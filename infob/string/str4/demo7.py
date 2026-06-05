n=input("enter the string :- ")
i=0
s=""
s1=""
while i<len(n):
    ch=n[i]
    if ch!=" " :
        s=s+ch
        if ch==n[-1]:
            if s not in s1:
             s1=s1+s+" "
    else:
        if s not in s1:
            s1=s1+s+" "
            s=""
        else:
            s=""
    i=i+1
print(s1)