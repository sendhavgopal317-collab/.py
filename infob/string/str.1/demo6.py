n=input("enter PNR ")
i=-1
l=len(n)
if len(n)!=12 or n[0]!="P" or n[1]!='N' or n[2]!='R':
    print("invalid PNR")
else:  
 while i>=(-9):
    ch=n[i]
    if ch not  in "1234567890":
     print("enter valid PNR")
     break
    i=i-1
 else:
  print("valid PNR")
