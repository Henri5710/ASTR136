from __future__ import print_function, absolute_import, division, unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt

def makeArray(size):
	
	#Create Array with proper size, mean, and RMS:
	pArr = np.random.normal(1,2,size)
	
	return pArr

def plotArr(pArr, binSize):
	
	#plot the histogram of the randomly generated data
	count, bins, ignored = plt.hist(pArr, binSize, density = True, color = 'purple')

	#Plot the associated Gaussian distribution
	plt.plot(bins, 1/(2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 1)**2 / (2 * 2**2) ), linewidth = 2, color = 'green')
	
	#Display graph/save figure as PDF
	plt.show()
	plt.savefig("Assignment1_ASTR136_Henri_Geneste_1675311_Plot.pdf")
	return

#Create the array:
myArr = makeArray(1000)

#Check mean and RMS of array:
print('The mean is: ', np.mean(myArr))
print('The RMS is: ', np.std(myArr))

#Plot random array using a specified number of bins (in this case I chose 10)
plotArr(myArr,10)