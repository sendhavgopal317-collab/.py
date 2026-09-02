pages=["home","about","home","contact","home","about"]
d={}
for x in pages:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k, "visited ",v)