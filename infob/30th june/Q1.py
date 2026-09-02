import math
n=int(input())
temp=n
sum=0
rev=0
digit=0
while n>0:
    digit=n%10
    sum=sum+digit
    rev=rev*10+digit
    n=n//10
diff=abs(temp-rev)
final_result=sum+diff
print("rev: ", rev)
print("sum=",sum)
print("diff ",diff)
print("final result ",final_result)
if final_result<2:
    print("not prime")
i=2
while i<=(math.sqrt(final_result)):
    if final_result%i==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime")   



