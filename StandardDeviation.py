#Standard deviation
import math

data=[12,18,14,20,16]
n=len(data)
mean=sum(data)/n
variance=sum((x-mean)** 2 for x in data)/n
std_deviation=math.sqrt(variance)
print(f"Standard deviation:{std_deviation}")
