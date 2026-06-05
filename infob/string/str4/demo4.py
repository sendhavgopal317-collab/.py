n=input("enter the string ")
s=""
s1=n
i=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
     while i<len(n):
      ch=n[i]
      if ch!=" ":
        s=s+ch
      else:
        if len(s)<len(s1):
            s1=s
            s=""
      i=i+1
    i=i+1
print(" smallest word is :- ",s1)
        

       
