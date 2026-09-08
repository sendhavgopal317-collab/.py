'''55 Reverse only vowels.S = "hello""holle"'''
s=input("enter -- ")
s1=""
count=0
for i in range(len(s)-1,0,-1):
   if s[i] not in "aeiou":
    s1=s[i]+s1
   else:
   
     for j in range(len(s)):
       if s[j] in "aeiou":
        s1=s1+s[j]
        break
print(s1)
      
