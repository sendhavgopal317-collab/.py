'''7Convert a string to lowercase.  
S = "HELLO" "hello"'''
s=input("enter str ")
s1=""
for i in s:
    if i>"a" and i<"z":
        s1+=i
    else:
        s1=s1+(chr(ord(i)+32))
print(s1)
    
