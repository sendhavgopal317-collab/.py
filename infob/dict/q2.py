l=["it","it","hr","sales","finance"]
d={}
for department in l:
    d[department]=d.get(department,0)+1
print(d)
for k,v in d.items():
    print(k," has ",v ," employees")