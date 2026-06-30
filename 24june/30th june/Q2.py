import math
n=int(input("enter number = "))
temp=n
product=1
sum=0
count=0
while n>0:
    digit=n%10
    sum=sum+digit
    count=count+1
    product=product*digit
    n=n//10
print("product = " , product)
print("sum = ", sum)
diff=abs(product-sum)
print("diff = ", diff)
l=len(str(diff))
final=diff+l
print("final result= ",final)
if final<2:
    print("not prime")
else:  
    i=2
    while i>= (math.sqrt(final)) :
         if final%i==0:   
             print("not prime")
             break
         i=i+1
    else:
        print("prime")      