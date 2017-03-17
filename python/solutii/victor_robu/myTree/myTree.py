#!/usr/bin/env python
# *-* coding: UTF-8 *-*
import os

def myTree(Directory,nivel=0,StivaSimboluri=[]):
   if nivel==0:
	print(".")
   if os.path.isdir(Directory):
	lista=os.listdir(Directory)
	lista.sort()
	for name in lista:
	    for i in range(nivel+1):
		print("\t"),
	    print(name)
	    myTree(os.path.join(Directory,name),nivel+1)

def main():
   myTree(".")
   	
if __name__ == "__main__":
   main()
