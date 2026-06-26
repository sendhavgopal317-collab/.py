n=int(input("enter the num: "))
count=0
while n>0:
    d=n%10
    if d%2!=0:
        count=count+1
    n=n//10
print(count)        
