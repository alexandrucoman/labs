from __future__ import print_function
import os

topdir = 'C:\\Users\\Stefan\\Okay'
letter = 'a'

def step(letter, dirname, names):
	'''
	:param ext: The text to find in filename
	:param dirname: The directory name
	:param names: all files
	:return: Returns all files which contain the ext
	'''
	letter = letter.lower()
        for name in names:
            if name.lower().__contains__(letter):
                print(os.path.join(dirname, name))


def main():
    os.path.walk(topdir, step, letter)

if __name__ == "__main__":
    main()

