'''47 Check for substring using concatenation trick.
S1="CDAB", S2="ABCD"True (S1 is in S2+S2)'''
s1=input("enter rotated string").lower()
s2=input("enter main string ").lower()
if s1 in (s2+s2):
 print ("true ")
else:
 print("false")
 
