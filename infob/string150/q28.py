'''Find the first occurrence of a word.
S = "Test this test", Word = "test"10 (index)'''
n=input("enter string--")
w=input("enter word--")
if w in n:
    print("first occurence of word is at index=",n.index(w))