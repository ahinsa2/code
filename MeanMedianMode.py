#mean  
data=[12,18,14,20,16]
n=len(data)
mean=sum(data)/n
print(f"mean: {mean}")

#median
#sortedData=data.sort() DOUBT WHY IS THIS NOT WORKING?
sortedData=sorted(data)
print(sortedData)
median=(sortedData[n//2]+sortedData[(n-1)//2])/2
print(f"Median: {median}")

#mode
from statistics import mode
modeValue=mode(data)
print(f"mode: {modeValue}")

print()
#Standard deviation
import math
variance=sum((x-mean)** 2 for x in data)/n
std_deviation=math.sqrt(variance)
print(f"Standard deviation:{std_deviation}")

print()

#percentiles
import numpy as np
import matplotlib.pyplot as plt

p_25=np.percentile(data,25)
p_50=np.percentile(data,50)
p_75=np.percentile(data,75)
print(f"25th percentile: {p_25}")
print(f"50th percentile: {p_50} This is also the median.")
print(f"75th percentile: {p_75}")

plt.boxplot(data)
plt.title("GRAPH 1: box plot with percentile")
plt.xlabel("Data")
plt.ylabel("Value")
plt.show()



