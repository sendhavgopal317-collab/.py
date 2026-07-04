n1=int(input("enter the num1: "))
n2=int(input("enter the num2: "))
sum=0
for i in range(1,n2+1):
  if i==n2:
    sum=sum+n1**n2
  i=i+1
print(sum)    