n=int(input("enter first number"))
n1=int(input("enter second number"))
count=0
while n<=n1:
    if n%7==0:
        count = count+1
    n=n+1
print (count)    