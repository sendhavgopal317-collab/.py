n= int(input(" enter number :-"))
i=1
for i  in  range(n+1):
    j=1
    for j in range(i+1):
       if j==0 or j==i or i==n: 
        print("*",end="")
       else:
          print(" ",end="") 
    print()