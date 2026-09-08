'''29 Remove occurrences of a word.
S = "a test b test c", Word = "test", Remove All"a b c"'''
n=input("enter string--")
w=input("enter word--")
if w in n:
    print("removed all accurence of word=",n.replace(w,""))
else:
    print("word not found")