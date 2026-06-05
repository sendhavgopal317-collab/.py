n=int(input(" "))
for i in range(1,n+1):
    s=n
    while s>(i):
     print(" ",end="")
     s=s-1
    j=1
    for j in range(1,2*i):
     if i==1 or i==n:
       print("1",end="")
     else:
        if j==1 or j==i*2-1:
           print("1",end="")
        else:
          print("*",end="")
          
      
    print()