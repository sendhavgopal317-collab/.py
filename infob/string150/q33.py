'''33 Find the longest word
.S = "find the longest word""longest"'''
n=input("enter string--").split()
longest=""
for i in n:
    if len(i) > len(longest):
        longest = i
print(longest)