'''46 Check if a substring appears at both the start and end.S = "abcabca", Sub="abca"
true'''
s=input("enter string ")
sub=input("enter substring ")
if s.startswith(sub) and s.endswith(sub):
 print("true")
else:
 print("false")
