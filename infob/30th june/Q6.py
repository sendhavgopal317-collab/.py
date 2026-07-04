import math
n=int(input("enter num = "))
while True:
    n=n+1
    m=int(math.sqrt(n))
    if n<2:
       continue
    else:
       for i in range(2,m+1):
          if n%i==0:
            break
       else: 
         print(n)
         break         
            
