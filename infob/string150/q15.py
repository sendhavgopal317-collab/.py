s=input("enter ")
ch=input("enter character ")
for i in range(len(s)):
    if s[i]==ch:
        print(i , " first occureance of ",s[i])
        break