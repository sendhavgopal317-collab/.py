sales=["mobile","laptop","mobile","tablet","laptop","mobile"]
d={}
for x in sales:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k,":",v)