'''0 Replace a word with another word
.S = "old data", Old="old", New="new""new data"'''
n=input("enter string")
old=input("enter old data ")
new=input("enter new data")
if old in n:
    print(n.replace(old,new))

else:
    print("old not found")