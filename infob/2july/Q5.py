a=int(input("enter first number  : "))
b= int(input("enter second number : "))
for i in range (a,b+1):
    temp=i
    sum=0
    while temp>0:
        d=temp%10
        fact=1
        while d>0:
            fact=d*fact
            d=d-1
        sum=sum+fact
        temp=temp//10
    if sum==i:  
            print(i)  