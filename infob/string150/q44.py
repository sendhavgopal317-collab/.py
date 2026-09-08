'''44 Check if two strings are anagrams.
S1 = "listen", S2 = "silent"
true'''
s1=input("enter string 1 ")
s2=input("enter string 2 ")
if len(s1)!=len(s2):
  print("not anagram ")
else:
 if sorted(s1)!=sorted(s2):
  print("not anagram")
 else:
  print("anagram")
