n=int(input("enter number = "))
count=0
while n>0:
    d1=n%10
    n=n//10
    d2=n%10
    if d1<=d2:
        print("unstable num")
        count=count+1
        break
else:
    if count<=1:
        print("stable number ")
