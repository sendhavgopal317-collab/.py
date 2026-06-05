n=int(input(" "))
for i in range(1,n+1):
    s=n
    while s>(i-1):
     print("*",end="")
     s=s-1
    j=1
    for j in range(1,2*i):
       print(" ",end="")
    k=n
    while k>(i-1):
     print("*",end="")
     k=k-1

    print()