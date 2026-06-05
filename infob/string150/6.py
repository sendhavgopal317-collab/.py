'''6Convert a string to uppercase. 
 S = "hello" "HELLO"'''
s=input("enter str ")
s1=""
for i in s:
    if i>"A" and i<"Z":
        s1+=i
    else:
        s1=s1+(chr(ord(i)-32))
print(s1)
    
