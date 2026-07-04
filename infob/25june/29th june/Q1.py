import math
n=int(input(""))
if n<=1:
    print("not prime")
else:    
    i=2
    while i<=int(math.sqrt(n)) : 
           if n%i==0:
                print("not prime ")
                break
           i=i+1
    else:
         print("prime number")    