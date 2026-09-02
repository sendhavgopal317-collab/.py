n=int(input("enter number"))
square=n**2
temp=n
while temp>0:
    if temp%10!=square%10:
        print("not automophic number")
        break
    temp=temp//10
    square=square//10
else:
    print("automorphic num")
