n=int(input(" "))
for i in range(n,0,-1):
    s=1
    while s<n-i+1:
     print(" ",end="")
     s=s+1
    j=1
    for j in range(1,i*2):
     if i==1 or i==n:
       print(j,end="")
     else:
        if j==1 or j==i*2-1:
           print(j,end="")
        else:
          print("*",end="")
    print()