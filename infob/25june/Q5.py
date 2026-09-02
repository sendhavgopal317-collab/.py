n=int(input("enter the num"))
count=0
for i in range(1,n+1):
    if n%i==0:
     count=count+1
    i=i+1
print("factor count:", count)   