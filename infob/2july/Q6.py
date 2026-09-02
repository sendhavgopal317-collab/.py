n=int(input("enter  "))
m=int(input("enter  "))
for i in range(n,m+1):
    temp=i
    rev=0
    while temp>0:
        d=temp%10
        rev=10*rev+d
        temp=temp//10
    if rev==i:
        print(i)