

import lab4
import cv2
import numpy as np
from matplotlib import pyplot as plt

level = 50
filename = 'rose'
full = filename+'.jpg'
histoRGB =[]
histoYUV =[]
histoHSV =[]

for num in range(1,11):
	lab4.histogramlistAdd(histoRGB, str(num), 'RGB',level)
	lab4.histogramlistAdd(histoYUV, str(num), 'YUV',level)
	lab4.histogramlistAdd(histoHSV, str(num), 'HSV',level)

print len(histoRGB[2])
print len(histoYUV[2])
print len(histoHSV[2])

image4 = lab4.query(filename,histoRGB, 'RGB',level,'I')

out = lab4.rank(image4) 
print out



f = open('RGB-City.html','w')
header = '<table style="width:100%">\n<tr>'
##footer = 
f.write(header)
message1 = "<img src="
message2 = '.jpg ><br><p>'
message3 = '</p>'
for image in range(0,10):
	message = header+ message1 + str(out[image]+1) + message2 + str(image+1) + message3
	f.write(message)
f.close() 

image = cv2.imread(full)


color = ('b','g','r')
for i,col in enumerate(color):
	histr = cv2.calcHist([image],[i],None,[level],[0,level])
	plt.plot(histr,color = col)
	plt.xlim([0,level])
plt.show()