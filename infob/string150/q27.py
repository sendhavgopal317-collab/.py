
'''27 Find the last occurrence of a word.S = "Test this test", Word = "test"15 (index)'''
n=input("enter string--")
w=input("enter word--")
if w in n:
    print("last occurence of word is at index=",n.rfind(w)+len(w)+1)