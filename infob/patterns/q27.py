n=int(input(" "))
for i in range(n,0,-1):
    s=1
    while s<n-i+2:
     print("*",end="")
     s=s+1
    j=1
    for j in range(1,i*2):
     
       print("#",end="")
    for k in range (n-i+1):
       print("*",end="")
     
    print()