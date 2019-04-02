from __future__ import print_function, absolute_import, division, unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt
import random as random
#Inputs a data array of any size (type float)
def makeArray(size):
	#Create Array with proper size and type
	pArr = np.empty(size, dtype = float)
	
	mean_rms = False
	while not mean_rms:
		total = 0.0
		totalrms = 0.0
		
		#Populate Array
		for i in range(0,size):
			pArr[i] = random.uniform(-2,4)
			total = total + pArr[i]
			totalrms = totalrms + pArr[i]**2
		
		#Check for proper mean and RMS values (rounded)
		print('Mean is: ', round(total/size))
		print('RMS is: ', round(np.sqrt(totalrms/size)))
		if round((total/size)) == 1.0:
			if round(np.sqrt(totalrms/size)) == 2.0:
				mean_rms = True
			else:
				mean_rms = False
	return pArr

#Plots the array as a histogram with an inputted bin size
def plotArr(pArr, binSize):
	binNum = int(6/binSize)
	plt.hist(pArr, bins = binNum, range = (-2,4))
	plt.show()
	return
#Overplots the Gaussian that best describes the data

#Generates a postscript/PDF file of the plot

myArr = makeArray(1000)
print(myArr)
plotArr(myArr,0.5)