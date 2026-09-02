s=input("enter ")
ch=input("enter character ")
count=0

for i in range(len(s)-1,0,-1):
    if s[i]==ch:
        count+=1
print(count)
        