'''42 Check if two strings are equal without equals()
.S1 = "abc", S2 = "abc"TRUE'''
s=input("enter string ")
s1=input("enter 2 string ")
if len(s)!=len(s1):
 print("false")
else:
 for i in range(len(s)):
  if s[i]!=s1[i]:
    print("false")
    break
 else:
   print("true")
