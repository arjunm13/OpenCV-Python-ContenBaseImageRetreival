

import lab4
import cv2
import numpy as np
from matplotlib import pyplot as plt

### init number of levels and Query file name
numberOfLevels = 50
fileName = 'rose'
fullFileName = fileName+'.jpg'
histoRGB =[]
histoYUV =[]
histoHSV =[]

for num in range(1,11):
	lab4.histogramlistAdd(histoRGB, str(num), 'RGB',numberOfLevels)
	lab4.histogramlistAdd(histoYUV, str(num), 'YUV',numberOfLevels)
	lab4.histogramlistAdd(histoHSV, str(num), 'HSV',numberOfLevels)

### Config desired settings 
image4 = lab4.query(fileName,histoRGB, 'RGB',numberOfLevels,'I')

out = lab4.rank(image4) 
print out

### Create an HTML output that Orders the images depending on their 
### Similarity to the query Image

f = open('RGB-City.html','w')
header = '<table style="width:100%">\n<tr>'
##Header = 
f.write(header)
message1 = "<img src="
message2 = '.jpg ><br><p>'
message3 = '</p>'
for image in range(0,10):
	message = header+ message1 + str(out[image]+1) + message2 + str(image+1) + message3
	f.write(message)
f.close() 
