n=int(input(" "))
i=1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
          print(j, end=" ")
          j=j+1
    s=1
    while s<=(n-i)*2:
        print("*",end=" ")
        s=s+1
    k=i
    while k>=1:
         print(k,end=" ")
         k=k-1
    i=i+1