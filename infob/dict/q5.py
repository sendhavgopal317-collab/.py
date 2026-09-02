tags=["python","java","api","react","html","css"]
d={}
d1={}
for x in tags:
    length=len(x)
    if length not in d:
        d[length]=[]
    d[length].append(x)

for k,v in sorted(d.items()):
    d1[k]=v
print(d1)


    