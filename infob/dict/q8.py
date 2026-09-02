books=["python","python","java","api","react","html","css"]
d={}
d1={}
for x in books:
    d[x]=d.get(x,0)+1
print(d)
for k,v in sorted(d.items()):
    print(k," is issued ", v,"times ")



    