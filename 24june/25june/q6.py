n=int(input("enter the num: "))
sum=0
i=1
while n>=i:
    if n%i==0:
        sum=sum+i
    i=i+1
print(sum)          