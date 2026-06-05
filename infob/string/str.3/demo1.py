n=input("enter your name ")
i=0
s=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
        if s==0:
            print(ch.upper(),end="")
            s=1
    else:
        s=0
    i=i+1   
