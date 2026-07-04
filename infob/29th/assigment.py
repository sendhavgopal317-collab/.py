u=int(input("enter units"))
if u<=100:
    print("bill:",u*5)
elif u>100:
    print("bill:", (u-100)*7+100*5)
elif u<=200:
    print("bill:", (u-200)*10+100*7+100*5)         