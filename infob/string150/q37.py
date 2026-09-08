'''37 Reverse each word
.S = "cat dog""tac god"'''
n=input("enter string--").split()
rev=""
for i in n:
   rev=rev+("".join(i[::-1]))+" "
print(rev)
