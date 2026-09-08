'''50 Remove all digits.S = "a1b2c3""abc"'''
s=input("enter string")
s1=""
for i in s:
 if i in "1234567890":
  pass
 else:
   s1=s1+i
print(s1)
