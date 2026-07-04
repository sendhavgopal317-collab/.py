n=int(input("enter the num: "))
d=len(str(n))
while n>0:
    f=d%10
    if n==d:
        print(d)
    n=n//10    