n=int(input("enter number ; "))
temp=n
count=0
for i in range(len(str(n))):
    num = n%10
    n=n//10
    if n%2==0:
     count+=1 
if count==len(str(temp)):
        print("all are even")
else:
    print("not all even")        