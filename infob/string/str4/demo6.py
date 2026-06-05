n=input("enter the string ")
w=input("enter the word")
i=0
s=""
count=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
        s=s+ch
    elif s==w:
            count=count+1
            s=""
    else:
         s=""

    i=i+1
print("we found string --", count , " times")