orders=["pizza","pasta","pizza","burger","burger","pizza","pasta","pizza","pasta"]
d={}
for x in orders:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k,":",v)