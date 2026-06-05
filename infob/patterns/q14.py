
n=int(input("enter number"))
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ",end="")
        space=space+1
    j=1
    while j<=i:
        if i%2==0:
            if j%2==0:
             print("0",end="")
            else:
               print("1",end="")
        if i%2!=0:
           if j%2!=0:
              print("1",end="")
           else:
              print("0", end="")
        j=j+1
    print()
    i=i+1     