n= input("enter bank account number ")
i=-1
l=len(n)-4
s=""
while i>-l-4:
    ch=n[i]
    if i>-l:
     print("*",end="")
    else:
       print(ch,end="")

    i=i-1