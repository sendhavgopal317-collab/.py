n=input("enter the product code")
temp=""
l=len(n)
i=-1 
while i>-l-1:
    ch=n[i]
    temp=temp+ch
    i=i-1
if temp==n:
    print (n, "is polindrom")
else:
    print(n ,"is not polindrom")
