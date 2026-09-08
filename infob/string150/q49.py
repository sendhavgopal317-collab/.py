'''49 Replace all consonants with '*' (Example suggests replacing non-vowels).S = "apple""ap*le" (or similar output depending on i'''
s=input(" enter string  ")
s1=""
for i in range(len(s)):
 if s[i] in "bcdfghjklmnpqrstvwxyz" and s[i]==s[i-1]:
  s1=s1+"*"
 else:
  s1=s1+s[i]
print(s1)
