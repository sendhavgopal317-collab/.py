n=int(input("enter number ; "))
count=0
for i in range(len(str(n))):
    num = n%10
    n=n//10
    if n%2!=0:
     count+=1
print(count)