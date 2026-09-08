'''23 Print all characters that occur exactly
 twice.S = "aabbcdee"b', 'e'''
n=input("enter string")
checked=""
for i in n:
    if n.count(i)==2 and i not in checked:
        print(i)
        print("is repeating twice")
        checked+=i