s=input("enter string ")
ind=int(input("enter index "))
for i in range(len(s)):
    if i==ind:
        print(ord(s[i-1]))