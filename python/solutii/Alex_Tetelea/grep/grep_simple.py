"""Grep Simple problem"""
import getopt
import os
import re
import sys


def search2(
        src, casesensitive, exact=False,
        find_str="", shouldreplace=False,
        replaceable="", param_n=False
):
    """Functie pentru cautarea fisierelor similar comenzei GREP
    :param src:
    :param param_n:
    :param replaceable:
    :param shouldreplace:
    :param find_str:
    :param exact:
    :param casesensitive:
    """
    message = src.read()
    allteorems = []
    message.split()
    lista = re.split(r'\d+\.  ', message)
    lista.pop(0)
    for teorema in lista:
        seaparator = teorema.split("  |- ")
        iteorema = {r"Nume_complet": seaparator[0].strip().split('\n')[0],
                    r"Nume_scurt": seaparator[0].strip().split('\n')[1],
                    r"Descriere": seaparator[1::],
                    r"Tot_mesajul": teorema}
        allteorems.append(iteorema)
    good_theorems = []
    count = 0
    for teorema in allteorems:
        if casesensitive:
            if exact:
                found = re.findall(r"\s" + find_str + r"\s",
                                   teorema["Tot_mesajul"])
            else:
                found = re.findall(find_str, teorema["Tot_mesajul"])
        else:
            if exact:
                found = re.findall(r"\s" + find_str + r"\s",
                                   teorema["Tot_mesajul"], re.IGNORECASE)
            else:
                found = re.findall(find_str,
                                   teorema["Tot_mesajul"], re.IGNORECASE)
        if len(found) > 0:
            count += len(found)
            good_theorems.append(teorema)
    if exact or not casesensitive:
        if len(good_theorems) < 2:
            for teorema in good_theorems:
                print teorema["Tot_mesajul"]
        else:
            for teorema in good_theorems:
                print teorema["Nume_complet"], teorema["Nume_scurt"]

    if shouldreplace:
        if casesensitive:
            insensitive_hippo = re.compile(re.escape(find_str))
            if exact:
                message = insensitive_hippo.sub(r"\s" +
                                                replaceable + r"\s", message)
            else:
                message = insensitive_hippo.sub(replaceable, message)

        else:
            insensitive_hippo = re.compile(re.escape(find_str),
                                           re.IGNORECASE)
            if exact:
                message = insensitive_hippo.sub(r"\s" +
                                                replaceable + r"\s", message)
            else:
                message = insensitive_hippo.sub(replaceable, message)
        src.seek(0)
        src.write(message)
        src.truncate()
        src.close()
    if param_n:
        print count
    pass


def main(argv):
    """Prima functie ce va fi rulata"""

    if len(argv) == 0:
        print(
            'grep_simple.py [-i - case insensitive]'
            ' [-param_e - exact] [-s - replace] [-n - count] '
            '[-r] [Folder_name] | [file_name]'
        )
        sys.exit()
    try:
        options = ' '.join(argv).split(' ')[0]
    except getopt.GetoptError:
        print r"Eraore"
    param_i = False
    param_e = False
    param_S = False
    param_n = False
    param_r = False
    for opt in options:
        if opt[0] == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt[0] in "i":
            param_i = True
        elif opt in "param_e":
            param_e = True
        elif opt in "s":
            param_S = True
        elif opt in "n":
            param_n = True
        elif opt in "r":
            param_r = True
        elif opt in "h":
            print 'grep_simple.py ' \
                  '[-i - case insensitive] ' \
                  '[-param_e - exact] [-s - replace] ' \
                  '[-n - count] ' \
                  '[-r] [Folder_name] | [file_name]'
    replace = ""

    if not param_r:
        if not param_S:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        read_file = open(argv[-1], 'r+')
        phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
        search2(read_file, not param_i,
                param_e, phrase, param_S,
                replace, param_n)
    else:
        if not param_S:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        for folder, subs, files in os.walk(argv[-1]):
            for filename in files:
                with open(os.path.join(folder, filename), 'r+') as src:
                    phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
                    search2(src, not param_i, param_e,
                            phrase, param_S, replace, param_n)


if __name__ == "__main__":
    """Enter point"""
    main(sys.argv[1:])
