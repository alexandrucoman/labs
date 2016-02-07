#!/usr/bin/env python
# *-* coding: UTF-8 *-*


ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}

def inversare_dictionar():
	d=dict()
	for key, value in ICAO.items():
		d[value]=key
	return d


def din_icao(string):
	Alfabet=inversare_dictionar()
	lista= list()
	for i in string.split():
		if i in Alfabet:
			lista.append(Alfabet[i])
	return "".join(lista)

def main():
	try:
		fisier=open("mesaj.icao", "r")
		mesaje=fisier.read()
		fisier.close()
	except IOError:
		print("Nu am putut obtine mesajele.")
		return

	for linie in mesaje.splitlines():
		print(din_icao(linie))

	
if __name__== "__main__":
	main()	



