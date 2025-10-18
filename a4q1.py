''' Write a code to simulate tossing a fair coin 1000 times. Count and display the number of heads and
 tails.'''
import random
head=0
tail=0
def toss(coinNo):
    
    for i in range (coinNo):
        
        if random.randint(1,2)<2:
            head+=1
        else:
            tail+=1
    return head ,tail
        
            
print(toss(1000))
             
