n=int(input("enter number"))
i=1
while i<=n:
    print(" "*(n-i),end="")
    if i>=2:
        print(11**(i),end=" ")
    else:
        print(i,end="")
    print()
    i=i+1

