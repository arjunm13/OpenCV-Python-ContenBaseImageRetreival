
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
from matplotlib import pyplot as plt

### Takes channel types as input and number of levels in the histogram 
def histogramlistAdd(histoindex, file, type, levels):
	## Create File name
	file = 'images/' +file + '.jpg'
	## read file 
	img = cv2.imread(file)

	if type == 'RGB':

		color = ('b','g','r')
		## Create a histogram for all channels (Concatinated)
		for i, col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[levels],[0,levels])
			histoindex.append(histr)
			
	##Same as above but for YUV
	if type == 'YUV':

		img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

		color = ('Y','U','V')

		for i, col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[levels],[0,levels])
			histoindex.append(histr)
	##Same as above but for HSV
	if type == 'HSV':

		img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

		color = ('H','S','v')

		for i in range(0,3):
			 if (i == 0):
			 	## H channel gets more levels 
				histr = cv2.calcHist([img],[i],None,[levels+25],[0,levels+25])
				histoindex.append(histr)
			 else:
				histr = cv2.calcHist([img],[i],None,[levels-25],[0,levels-25])
				histoindex.append(histr)
			
## Do cityBlock measurement calc
def cityblock(histo1, histo2):

	sum = 0
	for i in range(1,len(histo1)):
		sum = sum + abs(histo1[i] - histo2[i])

	return sum
## Do Eculidean measurement calc
def euclidean(histo1, histo2):

	sum = 0
	for i in range(1,len(histo1)):
		sum = sum + pow((histo1[i] - histo2[i]),2)
	return sum

## Normalize values in histogram, Needed for Histogram instesction
## calculations
def normalizer(histo1):
	norm = 0
	for i in range(1,len(histo1)):
		norm = norm + histo1[i]

	return norm


## Do histogram intersection calc
def histogramIntersection(histo1, histo2):

	sum = 0
	normal = 0

	for i in range(1,len(histo1)):
		sum = sum + min((abs(histo1[i]),abs(histo2[i])))

	normal = sum /(min(normalizer(histo1),normalizer(histo2)))
	return normal

def rank(input):
	temp = list(input)
	rank = []
	
	temp.sort()

	for i in range(0, len(temp)):
		for j in range(0, len(temp)):
			if (temp[i]==input[j]):
				rank.append(j)

	return rank
			

## Takes the File, channels type, # of levels and Distance Calculation type
## and performs query
def query(file, histoindex, type, levels, operation):

	CHANNELNUMBER = 3
	tempsum = 0

	currentHisto = []

	difference = []

	histogramlistAdd(currentHisto, str(file), type,levels)

	## Depending on the type of operation, The difference between the 
	## two images will be calculated and the difference value will be output
	## The output will be an array of values, The lower the difference the more
	## similar the image
	if operation == 'C':

		for i in range (0,(len(histoindex)/3)):
			for j in range(0,3):
				tempsum = tempsum + cityblock(currentHisto[j],histoindex[(i*CHANNELNUMBER)+j])
				sumnorm = sum(currentHisto[j])
				tempsum =  tempsum/sumnorm
			print tempsum	
			difference.append(tempsum)
			tempsum =0;
				

		return difference		

	if operation == 'E':
		for i in range (0,(len(histoindex)/3)):
			for j in range(0,3):
				tempsum = tempsum + euclidean(currentHisto[j],histoindex[(i*CHANNELNUMBER)+j]) 
				sumnorm = sum(currentHisto[j])
				sumnorm=pow(sumnorm,2)
				tempsum =  tempsum/sumnorm
			print tempsum	
			sumnorm =  sum(histoindex[i])
			#print sumnorm
			difference.append(tempsum)
			tempsum =0;
		return difference

	if operation == 'I':
		for i in range (0,(len(histoindex)/3)):
			for j in range(0,3):
				tempsum = tempsum + histogramIntersection(currentHisto[j],histoindex[(i*CHANNELNUMBER)+j]) 

			print tempsum
			difference.append(tempsum)
			tempsum =0;
	
		return difference
	


