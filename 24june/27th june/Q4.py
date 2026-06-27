n=int(input("enter number : "))
sum=0
temp=n
while temp>0:
    d=temp%10
    fact=1
    for i in range (1,d+1):
        fact=fact*i
    sum=fact+sum    
    temp=temp//10
if sum == n:
    print("strong num ")
else:
    print("not strong")                                                                          