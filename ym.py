m=int(input("Enter the month: "))
y=int(input("Enter the year: "))

match m:
    case 1|3|5|7|8|10|12:
        d=31
    case 2:
        if((y%4==0 and y%100!=0) or (y%400==0)):
            d=29
        else:
            d=28
    case 4|6|9|11:
        d=30
print(d)
