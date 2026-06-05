n=int(input("enter number "))
i=1
for i in range (n):
    for  j in range((n)+1):
        if j==i+1 or j==n-i :
         print("*",end="")
        else:
           print(" ",end="")
   
    print()