n=int(input("enter num "))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print(rev)




n=int(input("enter num "))
rev=0
for i in range (len(str(n))):
    rev=rev*10+n%10
    n=n//10
print(rev)   