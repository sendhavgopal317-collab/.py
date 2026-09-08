'''22 Find the last repeating character.
S = "abracadabra"r'''
s=input("enter string")
c=0
s1=""
for i in range(len(s)):
   c= s.count(s[i])
   if c<=1:
      r=(s[i])
