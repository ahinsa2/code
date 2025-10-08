#a=int(input("Enter the first number: "))
#b=int(input("Enter the second number: "))
a=15
b=5
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(i)
