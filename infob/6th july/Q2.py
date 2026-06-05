n=int(input("enter the number"))
count=0
sum=0
i=0
i1=1
print(i)
pre=0
while count<=n-2:
    if i1>0:
     i2=i1+i
     print(i1)
     count=count+1
     sum=sum+i1
     if i1>5:
        pre=pre+1
     i=i1
     i1=i2
print(sum)
print(pre)