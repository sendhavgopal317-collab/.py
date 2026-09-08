'''39 Search all occurrences of a character.
S = "banana", Char='a'1, 3, 5 (indices)'''
n=input("enter string ")
ch=input("enter character to found")
for i in range(len(n)):
   if n[i]==ch:
    print(i,end=" ")
