'''40 Search all occurrences of a word.
S = "a b a b", Word='b'2, 6 (start indices'''
s=input("enter string")
word=input("enter word")
for i in range(len(s)):
   if s[i]==word:
    print("index of word is ",i)
