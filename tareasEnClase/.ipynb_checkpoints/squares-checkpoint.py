#!usr/bin/python-3
import time


def square():
	length = int(input(">>"))

	for i in range(1, length+1):
		for j in range(1, length+1):
			if(i==1 or i==length or j==1 or j==length):
				print("#", end="")
			else: print(" ", end="")
		print('')

def main():
	while 1:
		square()

if __name__=='__main__':
	main()