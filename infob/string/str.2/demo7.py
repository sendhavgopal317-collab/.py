n=input ("enter information ")
i=0
s2=""
s=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
        if s==0:
            if ch>'a' and ch<'z':
             ch=ch.upper()
             s=1
    else:
       s=0
    i=i+1
    s2=s2+ch
print(s2)