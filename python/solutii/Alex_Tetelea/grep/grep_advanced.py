"""Exercitiu din seria GREP"""
from __future__ import print_function

import getopt
import os
import re
import sys
from BColors import BColors
from collections import Counter


def generator_1(message=""):
    """Generator for line separator"""
    return iter(message.splitlines())


def search2(read_file, phrase, replace,
            param_i, param_e, param_s,
            param_n, param_t, param_c):
    """

    :param param_c: Colloring
    :param param_t:
    :param param_n: Count
    :param replace: Substring cu care se va face inlocuirea
    :param param_s:
    :param phrase: Substring cautat
    :param param_e: Exact
    :param param_i: Case Insensitive
    :param read_file: Fisierul Din care se va citi
    :rtype: object
    """
    message = read_file.read()
    words = re.findall(r'\w+', message)  # This finds words in the document
    if param_s:
        if param_i:
            insensitive_hippo = re.compile(re.escape(phrase))
            if param_e:
                message = insensitive_hippo.sub(r"\s" +
                                                replace + r"\s", message)
            else:
                message = insensitive_hippo.sub(replace, message)

        else:
            insensitive_hippo = re.compile(re.escape(phrase),
                                           re.IGNORECASE)
            if param_e:
                message = insensitive_hippo.sub(r"\s" + replace +
                                                r"\s", message)
            else:
                message = insensitive_hippo.sub(replace, message)
        read_file.seek(0)
        read_file.write(message)
        read_file.truncate()
    read_file.close()
    list_lines = list(generator_1(message))
    lista = list_lines
    lista.pop(0)
    count = 0
    goodlines = []
    nr_line = 0
    teorema = ""
    for teorema in list_lines:
        if param_i:
            if param_e:
                element = re.findall(r"\s" + phrase + r"\s", teorema)
            else:
                element = re.findall(phrase, teorema)
        else:
            if param_e:
                element = re.findall(
                    r"\s" + phrase + r"\s", teorema, re.IGNORECASE)
            else:
                element = re.findall(phrase, teorema, re.IGNORECASE)
        nr_line += 1
        if len(element) > 0:
            count += len(element)
            goodlines.append((nr_line, teorema))
    if param_t:
        print("Top 5 cuvinte:")
        if not param_i:
            # capitalizes all the words
            cap_words = [word.lower() for word in words]
        else:
            # capitalizes all the words
            cap_words = [word for word in words]
            # counts the number each time element word appears
        word_counts = Counter(cap_words)
        for j in word_counts.most_common(5):
            print(j)
    if not len(goodlines):
        return
    if param_e or not param_i:
        if param_c:
            for teorema in goodlines:
                print(read_file.name, end=":")
                print(teorema[0], end=":")
                teorema = teorema[1]
                index = 0
                last = []
                for last in [(item.start(), item.end())
                             for item in list(re.finditer(phrase, teorema))]:
                    print(teorema[index:last[0]] +
                          BColors.FAIL + teorema[last[0]:last[1]] +
                          BColors.ENDC, end="")
                    index = last[1]
                print(teorema[last[1]:])

        else:
            print(teorema, end="")
    print("\n")
    if param_n:
        print("Numarul de apariti:", count)
    print("\n" + "#" * 100 + "\n")


def main(argv):
    """Main function in file"""
    opts = ""
    if len(argv) == 0:
        print(
            'grep_simple.py '
            '[-i - case insensitive] '
            '[-e - exact] '
            '[-s - replace] '
            '[-n - count] '
            '[-r] '
            '[Folder_name] | [file_name]',
            sep=""
        )
        sys.exit()
    try:
        opts = ' '.join(argv).split(' ')[0]
    except getopt.GetoptError:
        print("Eraore")
    param_i = False
    param_e = False
    param_s = False
    param_n = False
    param_r = False
    param_t = False
    param_c = False
    for opt in opts:
        if opt[0] == 'h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt[0] in "i":
            param_i = True
        if opt in "e":
            param_e = True
        elif opt in "s":
            param_s = True
        if opt in "n":
            param_n = True
        elif opt in "r":
            param_r = True
        if opt in "c":
            param_c = True
        elif opt in "t":
            param_t = True
        if opt in "h":
            print(
                'grep_simple.py '
                '[-i - case insensitive] '
                '[-e - exact] [-s - replace] '
                '[-n - count] [-r] '
                '[Folder_name] | [file_name]')
    replace = ""

    if not param_r:
        if not param_s:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        read_file = open(argv[-1], 'r+')
        phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
        search2(
            read_file, phrase, replace,
            not param_i, param_e, param_s,
            param_n, param_t, param_c)
    else:
        if not param_s:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        for folder, _, files in os.walk(argv[-1]):
            for filename in files:
                with open(os.path.join(folder, filename), 'r+') as src:
                    phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
                    search2(
                        src, phrase, replace,
                        not param_i, param_e, param_s,
                        param_n, param_t, param_c
                    )


if __name__ == "__main__":
    main(sys.argv[1:])
