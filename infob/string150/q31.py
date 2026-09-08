'''31 Remove duplicate words.
S = "the cat and the dog""the cat and dog"'''
n=input("enter string--").split()
new=[]
for i in n:
    if i not in new:
        new.append(i)
        print(" ".join(new))
       
