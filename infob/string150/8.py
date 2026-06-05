'''8Toggle the case of each character. 
S = "MiXED" "mIxeD"'''
s=input("enter str ")
s1=""
for i in s:
    if i>"a" and i<"z":
        s1=s1+(chr(ord(i)-32))
    else:
        s1=s1+(chr(ord(i)+32))
print(s1)
    
