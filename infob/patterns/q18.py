n=int(input(" "))
for i in range(0,n+1):
    s=n
    while s>(i):
     print(" ",end="")
     s=s-1
    j=1
    for j in range(1,2*i):
       print(11**i,end="")
    print()