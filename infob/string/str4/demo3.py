n=input("enter string :-- ")
i=0
while i<len(n):
    count=0
    ch=n[i]
    for x in n:
                if ch==x:
                  count=count+1   
    if count<2:
               print(ch ,end=" ")
            
    i=i+1