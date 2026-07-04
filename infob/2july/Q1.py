n=int(input("enter number :- "))
m=n
for n in range(1,m+1):
     for i in range(1,m+1):
          print (  n,"*", i, "=", i*n , end="    ")
     print()