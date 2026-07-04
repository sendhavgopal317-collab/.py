n=int(input("enter num :"))
d=int(input("enter digit"))
count=0
for i in range (len(str(n))):
    digit= n%10
    n=n//10
    if d==digit:
     count+=1
print(count)    