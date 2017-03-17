#!/bin/bash

if [[ $# -ne '2' ]];
then
	echo "Fisierul primeste 2 caractere. Exemplu :./$0 10 20"
	exit 1
fi

#if [[ ! -f script.sh ]];
#then
#	echo "Fisierul cu functii nu exista"
#	exit 1
#else
#	. script.sh
#fi
add()
{
rez="$(($1+$2))"
echo $rez
}

substract()
{
rez="$(($1-$2))"
echo $rez
}

multiply()
{
rez="$(($1*$2))"
echo $rez
}

divide()
{
rez="$(($1/$2))"
echo $rez
}

modulo()
{
rez="$(($1%$2))"
echo $rez
}

menu()
{
	echo "Meniu:"
	echo -e '\t' 1:Adunare
	echo -e '\t' 2:Scadere
	echo -e '\t' 3:Inmultire
	echo -e '\t' 4:Impartire
	echo -e '\t' 5:Modulo
	echo -e '\t' 0:Exit

	read -p 'Option: ' opt

	case "$opt" in
0)
	exit 0;
	;;
1)
	n="$(add "$1" "$2")"
	echo "$n"
	;;
2)
	n="$(substract "$1" "$2")"
	echo "$n"
	;;
3)
	n="$(multiply "$1" "$2")"
	echo "$n"
	;;
4)
	if [[ "$2" -eq '0' ]]; then
		echo "Al doilea parametru este 0. Iesim..."
		exit 1;
	else
		n="$(divide "$1" "$2")"
		echo "$n"
	fi
	;;
5)
	if [[ "$2" -eq '0' ]]; then
		echo "Al doilea parametru este 0. Iesim.."
		exit 1;
	else
		n="$(modulo "$1" "$2")"
		echo "$n"
	fi	
	;;
*)
	echo "Optiune invalida"
	exit 1;
	esac
}

menu "$1" "$2"

