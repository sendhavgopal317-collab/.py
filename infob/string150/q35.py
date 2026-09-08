'''35 Find the first palindrome word.
S = "this madam is here""madam"'''
n=input("enter string").split()
pol=""
for i in n:
 if i==i[::-1]:
  print(i , "is polindrom")
