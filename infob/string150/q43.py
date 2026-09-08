'''43 Check if two strings are rotations of each other
.S1 = "abcde", S2 = "cdeab"TRUE'''
s1=input("enter 1 string ")
s2=input("enter 2 string ")
d=len(s1)//2
s=""
for i in range(d):
  s=s+s1[i]
if s1.startswith(s) and s2.endswith(s):
 print ("true")
else:
 print("false")
