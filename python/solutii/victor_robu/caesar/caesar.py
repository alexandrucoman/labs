#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""
# pylint: disable=unused-argument

from __future__ import print_function

primCar=-1
def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    noOfChars = ord('z')-ord('a')+1
    global primCar
    if primCar < 0:
	for deplasare in range(noOfChars):
	    buf_list=[]
	    for litera in mesaj:
             	if litera.isalpha():
		    buf_list.append(chr((ord(litera)+deplasare-ord('a'))%noOfChars + ord('a'))) 
	        else:
		    buf_list.append(litera)
	    print("%d : %s"%(deplasare,"".join(buf_list)))
	flag = 1
	while flag:
	     print ("Alegeti unul din siruri introducand un numar intre 0 si",noOfChars-1)
	     try:
		opt=int(raw_input('Input:'))
	     except ValueError:
	     	print("Not a number")
	     else:
		if opt>=0 and opt<noOfChars:
		    flag=0
	primCar=(ord(mesaj[0])+opt-ord('a'))%noOfChars
    else:
	cheieInv=(primCar-ord(mesaj[0])+ord('a'))%noOfChars
	buf_list=[]
	for litera in mesaj:
	    if litera.isalpha():
		buf_list.append(chr((ord(litera)+cheieInv-ord('a'))%noOfChars + ord('a')))
	    else:
		buf_list.append(litera)
	print("Cheie  : %d. Mesaj : %s"%(noOfChars-cheieInv,"".join(buf_list)))

def main():
    """ Main function docstring """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return
    
    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
