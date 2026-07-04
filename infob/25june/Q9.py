n=int(input("enter the num: "))
s=n**2
l=len(str(n)) 
sum=0
while s>0:
    d=s%10
    sum=sum+d
    s=s//10
if sum==n:
    print("glowing succes") 
else:
    print("try again")       