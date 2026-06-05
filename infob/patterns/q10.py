n=int(input(""))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            if j%2==0:
             print("1",end="")
            else:
               print("0",end="")
        if i%2!=0:
           if j%2!=0:
              print("1",end="")
           else:
              print("0", end="")
              
        j=j+1
    i=i+1
        