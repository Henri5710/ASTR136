#ASTR 136 LECTURE 1
from __future__ import print_function, absolute_import, division, unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt
#% matplotlib inline

x = 7
print (x)

y = 2*x
print (y)

z = float(3)
print (type(z))
print(np.finfo(z))
print(np.sin(z))

myStr = "Hey"
myNewStr = myStr + "z"
print(myNewStr)

print(myStr.find('e'))

print(myStr == 'big')

print(myStr.replace(myStr[1],'i'))

myArr = np.empty(100, dtype = float)

print (len(myArr))

for i in range(0,100):
	myArr[i] = 1
print(myArr)

for i in range(0,100):
	myArr[i] = myArr[i] + 10
print(myArr)

for i in range (0,50):
	myArr[i] = myArr[i] + 100
print(myArr)

myArr2 = np.array([50] * 100, dtype = float)
print(myArr2)
print(len(myArr2))

myArr3 = myArr + myArr2
print(myArr3)

myArr4 = myArr * myArr2
print(myArr4)

myArr5 = np.array(range(0,100), dtype = float)
print(myArr5)
print(len(myArr5))

for i in range(0,100):
	if myArr5[i]%2 != 0:
		myArr5[i] = -1
print(myArr5)

plt.title('Sample Plot of Previously Declared Arrays')
plt.plot(myArr, linestyle = '-', color = 'purple')
plt.plot(myArr2, linestyle = '-.', color = 'green')
plt.plot(myArr3, linestyle = '--', color = 'black')
plt.plot(myArr4, linestyle = ':', color = 'red')
plt.show()

#plt.plot(myArr3, linestyle = 'x', color = 'black', label = 'Array 3')
#plt.plot(myArr4, linestyle = ';', color = 'red', label = 'Array 4')

myArr6 = np.array(range(-50,51), dtype = float)
print('Array 6:')
print(myArr6)