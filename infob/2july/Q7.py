n=int(input("enter  "))
m=int(input("enter  "))
for i in range(n,m+1):
    sum=0
    temp=i**2
    while temp>0:
        d=temp%10
        sum=sum+d
        temp=temp//10
    if sum==i:
        print(i)