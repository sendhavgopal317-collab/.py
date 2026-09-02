n=int(input("enter first number"))
n1=int(input("enter second number"))
for n in range(n,n1+1):
    sum=0
    i=1
    for i in range(1,n):
        if n%i==0:
         sum=sum+i
    if sum==n:
       print(n)     
        