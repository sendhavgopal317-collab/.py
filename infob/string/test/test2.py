s=input("enter string")
subs=""
i=-1
s1=""
for i in range( len(s)//2):
    s1=s1+s[i]
for i in range(len(s)-1):
  if s.startswith(s1) and s.endswith(s1):
   print(s1)
   break
  else:
     s1=s1.remove(s1[-1])
     
    
   
 
