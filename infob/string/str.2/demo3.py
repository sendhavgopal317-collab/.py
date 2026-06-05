n=input("enter youtr complaint ")
count=0
i=0
s=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
        if s==0:
            count=count+1
            s=1
    else:
        s=0
    i=i+1
print("Total wors are :-",count)