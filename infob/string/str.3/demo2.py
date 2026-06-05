n=input('enter message ')
i=0
s=0
j=""

while i<len(n):

     ch=n[i]
     if ch!=" ":
          if s==0:
               j=j+ch 
               s=1
          else:
               j=j+ch
               s=1
     else:
          if n[i]==" ":
              pass
          if n[i-1]!=" ":
               if i==1:
                    pass
               else:

                j=j+ch
        
          s=0
     i=i+1   
print(j)     