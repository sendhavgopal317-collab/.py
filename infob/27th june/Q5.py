n=int(input("enter number :- "))
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if temp%sum==0:
    print ("harshad number ")
else:
    print("its not harshad number")