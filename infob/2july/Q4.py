a=int(input("enter first number  :"))
b=int(input("enter second number  :"))
while a<10:
       a=a+1
       continue
for i in range(a,b+1):
           temp=i
           sum=0
           l=len(str(i))
           while temp>0:
               d=temp%10
               sum=sum+d**l
               temp=temp//10
           if i==sum:
                 print(i)