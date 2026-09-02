s=input("enter ")
large=0
new=""
for i in range(len(s)):
    if s.count(s[i])>large:
        large=s.count(s[i])
        x=(s[i]," is largest count " , large)
print(x)
