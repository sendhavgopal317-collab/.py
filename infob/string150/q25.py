'''24 Check if all characters in a string are unique.
S1 = "abc", S2 = "abca"S1: True, S2: False'''
n=input("enter string -")
for i in n:
    if n.count(i)>1:
        print("all characters  are not unique")
        break
else:
    print("all characters are unique")