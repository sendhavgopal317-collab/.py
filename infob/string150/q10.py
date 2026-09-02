s=input("enter string").strip()
new=""
for i in range(len(s)):
    if s[i]==" ":
        if s[i-1]==" ":
            pass
    else:
            if s[i-1]==" ":
                             new+=" "
            new+=s[i]
          
print(new)
