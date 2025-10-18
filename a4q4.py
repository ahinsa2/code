'''Given a bag with 3 red balls and 2 blue balls, write a program to find the probability
of drawing 2 red
 balls without replacement.'''
def ball(r,b):
    return (r/r+b)*(r-1/b+r-1)
print(ball(3,2))
    
