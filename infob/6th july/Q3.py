n=int(input("enter number"))
sum=0
product=1
while n>0:
    digit=n%10
    sum=sum+digit
    product=product*digit
    n=n//10
print("sum=",sum)
print("product:-",product)
if product==sum:
    print("spy number")
else:
  print("not spy number")