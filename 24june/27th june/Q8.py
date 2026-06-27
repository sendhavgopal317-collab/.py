n=int(input("enter number :- "))
rev=0
temp=n
while n>0:
    rev=rev*10+n%10
    n=n//10
print(rev)
diff=(rev-temp)
digit=len(str(diff))
print(diff)
if diff==0:
    print("perfect match")
elif diff%9==0:
    print("varified")