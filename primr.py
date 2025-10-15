'''a=int(input("Enter the lover limit: "))
b=int(input("Enter the upper limit: "))'''
a=4
b=10
for i in range (a,b+1):
    if i>2:
        for j in range (2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            print(i, end=" ")
