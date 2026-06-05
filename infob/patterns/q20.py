n=int(input(" "))
for i in range(1,n+1):
    s=n
    while s>(i):
     print(" ",end="")
     s=s-1
     ch=64
     j=1
    while j<=2*i-1:
       print(chr(ch+i),end="")
       if i==3 or i==4:
          print("   "*(i-2),end="")
          print(chr(ch+i),end="")
          break
       
       j=j+1
    print()