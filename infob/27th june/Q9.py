n=int(input("enter num :- "))
temp=n
digit1=0
digit2=0
diff=0
sum=0
largest=0
while n>1:
    digit1=n%10
    n=n//10
    digit2=n%10
    diff=abs(digit2-digit1)
    print(diff)
    sum=sum+diff
    if largest<diff:
        largest=diff
print(sum)
print(largest)
if sum%(len(str(temp)))==0:
    print("balance")
else:
    print("unbalanced")    