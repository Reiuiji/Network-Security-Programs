#Dan N
# HW 2: Caesar Cipher Utility
#Dependent: argparse
import os
import sys
import argparse

#input Parser
parser = argparse.ArgumentParser(description='HW 2 Caesar Cipher')
parser.add_argument("-i", "--input", dest='INPUT', help="Input File")
parser.add_argument("-o", "--output", dest='OUTPUT', help="Output File")
parser.add_argument("-b", "--basechar", dest='BASECHAR', help="Base Shift Char")
parser.add_argument("-s", "--shiftchar", dest='SHIFTCHAR', help="Shifted Char")
parser.add_argument("-l", "--loopmode", dest='LOOP', help="Enable Caesar Loop", action='store_true')

args = parser.parse_args()

if not args.BASECHAR:
	args.BASECHAR = raw_input("Base Character: ")
if not args.SHIFTCHAR:
	args.SHIFTCHAR = raw_input("Shift Character: ")
if not args.INPUT:
	INPUT = raw_input("Message: ")
else:
	if os.path.isfile(args.INPUT):
		f = open(args.INPUT, 'r')
		INPUT = f.read()
		f.close()
	else:
		print("Input File Does not Exist")
		sys.exit()

if args.LOOP:
	LOOP = args.LOOP
else:
	LOOP = False


def CaesarCipher(PlainText,Shift): 
	CipherText = ""
	for Char in PlainText:
		if Char.isalpha():
			A = ord(Char) + Shift
			if Char.islower():
				if A > ord('z'):
					A -= 26
			else:
				if A > ord('Z'):
					A -= 26
			CipherText += chr(A)
		else:
			CipherText += Char
	return CipherText

#Calculate the shift
Shift=ord(args.SHIFTCHAR.lower()) - ord(args.BASECHAR.lower())
if Shift < 0:
	Shift += 26
elif Shift > 26:
	Shift -= 26

if LOOP == False:
	CaesarOutput = CaesarCipher(INPUT, Shift)
	#Write Output
	if not args.OUTPUT:
		print(CaesarOutput)
	else:
		f = open('output.txt', 'w')
		f.write(CaesarOutput)
		f.close()
else:
	for a in range(26):
		CaesarOutput = CaesarCipher(INPUT, a)
		print(CaesarOutput)

