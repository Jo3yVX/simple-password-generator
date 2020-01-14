#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string

print(" ------- PASSWORD GENERATOR (8 - 16 chars) ---------")

UpperCase = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SpecialChar = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '|', '>', '<', ',', '.', '/', '?']

def GenChar(size, src):
	CharList = []
	while size != 0:
		CharList.append(random.choice(src))
		size -=1
	return CharList

def GenPass():
	#pass length: 10
	length = 10

	# number of char each type
	Size_Num = random.randrange(2,4)
	Size_Upper = random.randrange(2,4)
	Size_Lower = random.randrange(2,4)
	Size_Special = random.randrange(2,4)
	
	#gen pass
	RawPass = GenChar(Size_Num, Number) + GenChar(Size_Lower, LowerCase) + GenChar(Size_Special, SpecialChar) + GenChar(Size_Upper, UpperCase)
	random.shuffle(RawPass)
	return RawPass

def main():
	Pass = "".join(GenPass())
	print("Your Password is: ", Pass)
	return 0

if __name__ == "__main__":
	main()



