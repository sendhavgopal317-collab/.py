'''48 Remove all vowels.
S = "aeiou XYZ"" XYZ"'''
s=input("enter string").lower()
s1=""
for i in s:
  if i not in "aeiou":
   s1+=i
print(s1)

