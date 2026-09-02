s=input("enter ")
old=input("enter to replace ")
new=input("enter new ")
s1=""

for i in range(len(s)):
    if s[i]==old:
        s1+=new
    else:
        s1+=s[i]
print(s1)