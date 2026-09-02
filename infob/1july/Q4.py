a=int(input(""))
b=int(input(" "))
n=a
for n in range(a , b+1):
    fact=0
    for j in range(1,n//2+1):
        if n%j==0:
            fact=fact+j
    if fact==n:
        print(fact)