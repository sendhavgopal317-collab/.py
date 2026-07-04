n=int(input("enter num"))
m=1
while n>0:
    z=n%10
    m=z*m
    n=n//10

print(z)