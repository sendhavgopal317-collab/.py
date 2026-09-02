'''21 Find the first non-repeating character.
S = "aabbcde"c'''
s=input("enter string")
c=0
s1=""
for i in range(len(s)):
   c= s.count(s[i])
   if c<=1:
      print(s[i], "is first non repeated character ")
      break
