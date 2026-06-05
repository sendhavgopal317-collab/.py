n=int(input(" "))
for i in range(1,n+1):
    s=n
    while s>(i):
     print(" ",end="")
     s=s-1
     ch=64
     j=1
    while j<=2*i-1:
       print(chr(ch+j),end="")
       j=j+1
    print()