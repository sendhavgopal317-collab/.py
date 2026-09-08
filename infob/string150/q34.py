'''34 Find the shortest word.
S = "find the shortest word""the"'''
n=input("enter string").split()
shortest=(n[0])
for i in n:
   if len(i)<len(shortest):
       shortest=i
print(shortest)
