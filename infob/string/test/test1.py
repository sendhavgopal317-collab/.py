n=int(input("enter the number"))
i=0
temp=n
rev=0
count=0
while n>0:
    d=n%10
    rev=rev+d
    n=n//10
    print(d)
diff=abs(rev-temp)
while diff>0:
    d=diff%10
    count=count+1
    diff=diff//10
print("count is" , count)
if diff==0:
  print(" Perfect Match")
elif diff%9==0:
   print("varified")
else:
  print("rejected")
