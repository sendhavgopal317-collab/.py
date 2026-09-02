pages=["indore","bhopal","ujjain","indore","ujjain","indore"]
largest=0
d={}
for x in pages:
    d[x]=d.get(x,0)+1
    if d[x]>largest:
        largest=d[x]
        city=x
print(d)
print(city,largest)
for k,v in d.items():
    print(k, "downloads ",v)