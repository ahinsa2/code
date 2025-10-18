''' Write a code to simulate the rolling of two six-sided dice 5000 times
. Compute the experimental
 probability of getting a sum of 7'''
import random
def rolls(n):
    p=0
    for i in range (n):
        r1=random.randint(1,6)
        r2=random.randint(1,6)
        if r1+r2==7:
            p+=1
    return p/n
print(rolls(5000))        
