n1=int(input("enter the num1: "))
n2=int(input("enter the num2: "))
count=0
while n1<=n2:
    if n1%5==0:
        count=count+1
    n1=n1+1
print(count)