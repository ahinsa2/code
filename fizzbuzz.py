n=int(input('Enter a number between 1 to 100: '))
if n<=100:
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%5==0:
            print("Buzz")
        elif n%3==0 :        
            print("Fizz")
else :
     print("invalid input")
