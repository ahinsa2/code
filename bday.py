'''Write a program to simulate the birthday problem to find out the probability that in a group of 23
 people, at least 2 share the same birthday'''
import random
def bday(gNo):
    c=0
    for i in range (gNo):
        bdays=[random.randint(1,365)]
        if len (bdays)>len (set(bdays)):
            c+=1
        
    return c/gNo
        
print(bday(23))
