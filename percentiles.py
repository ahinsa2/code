#percentiles
import numpy as np
import matplotlib.pyplot as plt

data=[12,14,16,18,20]
p_25=np.percentile(data,25)
p_50=np.percentile(data,50)
p_75=np.percentile(data,75)
print(f"25th percentile: {p_25}")
print(f"50th percentile: {p_50} This is also the median.")
print(f"75th percentile: {p_75}")

plt.boxplot(data)
plt.title("box plot with percentile")
plt.xlabel("Data")
plt.ylabel("Value")
plt.show()
