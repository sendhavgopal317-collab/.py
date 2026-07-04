n=int(input("enter number = "))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//100
print(sum)    
