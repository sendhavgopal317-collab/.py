'''51 Extract only digits.S = "a1b2c3""123"'''
s=input("enter -- ")
s1=""
for i in s:
  if i in "1234567890":
   s1=s1+i
print(s1)
