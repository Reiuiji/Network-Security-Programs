#Daniel Noyes
# HW 1:
#Dependent on numpy, opencv, and argparse
import numpy as np
import cv2
import argparse
import os
import random
import binascii

#input Parser
parser = argparse.ArgumentParser(description='HW 1 Problem 1')
parser.add_argument("-i", "--input", dest='IMG', help="Image location")

args = parser.parse_args()

#INIT
if args.IMG:
	IMG = args.IMG
else:
	IMG = '{0}/{1}'.format(os.path.dirname(os.path.realpath(__file__)),'licenseplatefig7.jpg')

print IMG

DEBUG = True
USEShiftAlg = False
WritePic = False

#Setup random
#seed = os.urandom(32)
#Debug Seed
seed = 0x4bf3ebdddb87b417ab837ded40ce5c3ab5f8126d2722a18087c8991ef89477df

#print('seed : 0x{0}'.format(binascii.hexlify(seed)))
print('seed : {0}'.format(hex(seed)))

random.seed(seed)

#print('Random Number : {0}'.format(RndNum))


#Setup
img = cv2.imread(IMG)
cv2.imshow('Orig Image',img)

row = img.shape[0]
col = img.shape[1]

#Create Black/White Frame
ColorShift = np.zeros([row,col,3],dtype=np.uint8)
DarkFrame = np.zeros([row,col,3],dtype=np.uint8)
LightFrame = np.zeros([row,col,3],dtype=np.uint8)
RevealedFrame = np.zeros([row,col,3],dtype=np.uint8)
ScrambleFrame = np.zeros([row,col,3],dtype=np.uint8)
if(DEBUG == True):
	ScrambleDebug = np.zeros([row,col,3],dtype=np.uint8)
#Problem 1
RndNum = random.getrandbits(24)
for i in range(0,row):
	for j in range(0,col):
		R = (img[i,j,2] << 16)
		G = (img[i,j,1] << 8)
		B = img[i,j,0]
		C = R + G + B
		if(USEShiftAlg == True):
			#rotate C bits
			D = C
			A = ((C & 0xf00000) >> 20)
			C = ((C & 0x0fffff) << 4) + A

			ColorShift[i,j,2] = ((C & 0xff0000) >> 16)
			ColorShift[i,j,1] = ((C & 0x00ff00) >> 8)
			ColorShift[i,j,0] =  (C & 0x0000ff)

		else:
			S = C ^ RndNum

			#Interesting shift of color
			#ColorShift[i,j,2] = R+R*0.2
			#ColorShift[i,j,1] = G+G*0.2
			#ColorShift[i,j,0] = B+B*0.2

			#Demo Blue shift like DarkFrame:
			BF = ((S & 0xffff00) >> 8)
			ColorShift[i,j,0] = 0
			ColorShift[i,j,1] = ((BF & 0x00ff00) >> 8)
			ColorShift[i,j,2] = (BF & 0x0000ff)

		if( (j == 0) and (i == 0) and (DEBUG == True)):
			print('Debug: Shift Rotate')
			#print('  A: {0}'.format(hex(A)))
			print('  C: {0}'.format(hex(C)))
			#print('  D: {0}'.format(hex(D)))

cv2.imshow('ColorShift',ColorShift)

#Problem 2
#Hiding Routine
random.seed(seed)
for i in range(0,row):
	for j in range(0,col):
		if(USEShiftAlg == True):
			R = (ColorShift[i,j,2] << 16)
			G = (ColorShift[i,j,1] << 8)
			B = ColorShift[i,j,0]
			C = R + G + B
		else:
			R = (img[i,j,2] << 16)
			G = (img[i,j,1] << 8)
			B = img[i,j,0]
			C = R + G + B

		RndNum = random.getrandbits(24)
		S = C ^ RndNum
		if(DEBUG == True):
			#Debug Scrapbed Pixel Value
			ScrambleDebug[i,j,2] = ((S & 0xff0000) >> 16)
			ScrambleDebug[i,j,1] = ((S & 0x00ff00) >> 8)
			ScrambleDebug[i,j,0] =  (S & 0x0000ff)


		#Setup Black Frame:
		BF = ((S & 0xfff000) >> 12)
		DarkFrame[i,j,2] = 0
		DarkFrame[i,j,1] = ((BF & 0x000f00) >> 8)
		DarkFrame[i,j,0] =  (BF & 0x0000ff)

		#Setup White Frame:
		WF = (0xfff << 12) +  (S & 0x000fff) 
		LightFrame[i,j,2] = ((WF & 0xff0000) >> 16)
		LightFrame[i,j,1] = ((WF & 0x00ff00) >> 8)
		LightFrame[i,j,0] =  (WF & 0x0000ff)

		#Debug 1st to double check
		if( (j == 0) and (i == 0) and (DEBUG == True)):
			print('Debug: Hiding Routine')
			print('  C:  {0}'.format(hex(C)))
			print('  R:  {0}'.format(hex(RndNum)))
			print('  S:  {0}'.format(hex(S)))
			print('  BF: {0}'.format(hex(BF)))
			print('  WF: {0}'.format(hex(WF)))
			print('  R:  {0}'.format(hex(R)))
			print('  G:  {0}'.format(hex(G)))
			print('  B:  {0}'.format(hex(B)))

if(DEBUG == True):
	cv2.imshow('ScrambleDebug',ScrambleDebug)
cv2.imshow('DarkFrame',DarkFrame)
cv2.imshow('LightFrame',LightFrame)

#Problem 3
#Revealing Routine
#remake random (seed is the secret)
random.seed(seed)
for i in range(0,row):
	for j in range(0,col):
		BF = (DarkFrame[i,j,2] << 16) + (DarkFrame[i,j,1] << 8) + DarkFrame[i,j,0]
		WF = (LightFrame[i,j,2] << 16) + (LightFrame[i,j,1] << 8) + LightFrame[i,j,0]

		S = ((BF & 0x000fff) << 12) + (WF & 0x000fff)
		RndNum = random.getrandbits(24)
		P = S ^ RndNum

		if(USEShiftAlg == True):
			D = P
			A = ((P & 0x00000f) << 20)
			P = ((P & 0xfffff0) >> 4) + A


		#Debug Scrapbed Pixel Value
		ScrambleFrame[i,j,2] = ((S & 0xff0000) >> 16)
		ScrambleFrame[i,j,1] = ((S & 0x00ff00) >> 8)
		ScrambleFrame[i,j,0] =  (S & 0x0000ff)

		#Revealed License Plate
		RevealedFrame[i,j,2] = ((P & 0xff0000) >> 16)
		RevealedFrame[i,j,1] = ((P & 0x00ff00) >> 8)
		RevealedFrame[i,j,0] =  (P & 0x0000ff)

		#Debug 1st to double check
		if((j == 0) and (i == 0) and (DEBUG == True)):
			print('Debug: Reveal Routine')
			print('  BF: {0}'.format(hex(BF)))
			print('  WF: {0}'.format(hex(WF)))
			print('  S:  {0}'.format(hex(S)))
			print('  R:  {0}'.format(hex(RndNum)))
			print('  P:  {0}'.format(hex(P)))
			#print('  A: {0}'.format(hex(A)))
			#print('  D: {0}'.format(hex(D)))

cv2.imshow('ScrambleFrame',ScrambleFrame)
cv2.imshow('RevealedFrame',RevealedFrame)

#Write all images
if (WritePic == True):
	SaveLoc = os.path.expanduser('./HW1Pics')
	if not os.path.exists(SaveLoc):
		os.mkdir(SaveLoc)
	cv2.imwrite("{0}/Orig_Image.jpg".format(SaveLoc),img)
	cv2.imwrite("{0}/ColorShift.jpg".format(SaveLoc),ColorShift)
	if(DEBUG == True):
		cv2.imwrite("{0}/ScrambleDebug.jpg".format(SaveLoc),ScrambleDebug)
	cv2.imwrite("{0}/DarkFrame.jpg".format(SaveLoc),DarkFrame)
	cv2.imwrite("{0}/LightFrame.jpg".format(SaveLoc),LightFrame)
	cv2.imwrite("{0}/ScrambleFrame.jpg".format(SaveLoc),ScrambleFrame)
	cv2.imwrite("{0}/RevealedFrame.jpg".format(SaveLoc),RevealedFrame)


cv2.waitKey(0)
cv2.destroyAllWindows()

