n=input('enter the first product code ')
n1=input("enter second product code ")
i=0
x=1
visited=""
while i<len(n):
    ch=n[i]
    if ch==" " or ch not in "1234567890" or ch<'a' or ch>'z':
        pass
    elif ch not in visited:
     c=0
     c1=0
     j=0
     while j<len(n1):
        if n1[j]==ch:
            c=c+1
     j=0
     while j<len(n1):
        if n1[j]==ch:
            c1=c1+1
        j=j+1
     if c!=c1:
        x=0
        break
     visited.append(ch)
    i=i+1
if x==1:
    print("both are matching")
else:
    print("not matching")

