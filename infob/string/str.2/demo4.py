n=input("enter your employee id ")
i=3
if len(n)!=8 or n[0]!='E' or n[1]!='M' or n[2]!='P' :
    print("invalide employee id ")
else:
    while i<len(n):
        ch=n[i]
        if ch not in "1234567890":
         print("invalid employee id ")
         break
        i=i+1
    else :
       print(n ," is valid employee id")
           
        
