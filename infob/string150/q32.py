'''32 Count frequency of each word
.S = "apple banana apple"apple: 2, banana: 1'''
n=input("enter string--").split()
d={}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)