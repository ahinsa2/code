'''Write a program to simulate rolling a six-sided die 1000 times and calculate the probability of rolling
 a 6.'''
import random
def roll(n):
    c=0
    for i in range (1,6):
        if random.randint(1,6)==6:
            c+=1
    return c/n
print(roll(1000))
