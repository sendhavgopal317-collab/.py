'''45 Check whether a string starts/ends with another string
.S = "apple pie", Prefix = "apple", Suffix = "pie"
start:true , end :true'''
s=input("enter string ")
pre=input("enter prefix ")
suff=input("enter suff ")
if s.startswith(pre) and s.endswith(suff):
 print ("start:true end:true")
else:
 if s.startswith(pre) :
  print("start:true , end:false")
 elif s.endswith(suff):
  print("start:false , end:true")
 else:
  print("start:false. end :false")

