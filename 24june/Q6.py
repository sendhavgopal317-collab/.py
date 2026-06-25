n=int(input("enter num "))
temp=n
rev=0
sum=0
for i in range (len(str(n))):
    rev=n%10
    n=n//10
    sum=sum+rev*rev*rev
print(sum)    
if sum!=temp :    
  print(" not armstrong no.")   
else:
     print("armstrong no.")