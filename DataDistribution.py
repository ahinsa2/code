#DATA DISTRIBUTION

''' central tendency:where the center of data lies
shape of data:
NORMAL DISTRIBUTION: bellshaped symmetrical distribution.
ASYMMERTIC Distribution:
UNIFORM DISTRIBUTION

'''
import numpy as np
import matplotlib.pyplot as plt
data= np.random.normal(0,1,100)#(0,1,100)(loc,scale,size)
plt.hist(data, bins=30 ,edgecolor='black')#histogram
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

#mean
meanValue=np.mean(data)
medianValue=np.median(data)
stdDeviation=np.std(data)

print(f"Mean: {meanValue}")
print(f"Median: {medianValue}")
print(f"Standard Deviantion: {stdDeviation}")
