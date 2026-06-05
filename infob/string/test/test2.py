n=int(input("enter the number"))
diff=0
largest=0
sum=0
s=str(n)
while n>9:
   
   d=n%10
   n=n//10
   d1=n%10
   diff=abs(d1-d)
   print(diff,end="")
   sum=sum+diff
   if diff>largest:
     largest=diff
print("sum is ", sum)
print("largest", largest)
