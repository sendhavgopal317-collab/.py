n=int(input("enter number"))
cube=n**3
count=0
temp=0
while temp>0:
    if temp%10!=cube%10:
        print("not trimorphic number")
        break
    temp=temp//10
    cube=cube//10
else:
    print(n ,"is trimorphic number")