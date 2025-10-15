def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=24
b=16
print (gcd(a,b))
