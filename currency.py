#amt=int(input("Enter the ammout: "))
amt=370
h=amt//100
f=(amt % 100)//50
t= ((amt % 100)%50)//10
if ((((amt % 100)%50)%10)!=0):
    t+=1
print(h," Hundread rupee note ",f," fifty rupee note ",t," ten rupee note.")

