n=int(input("enter items "))
d={}
for i in range(n):
    key=input("enter product ")
    value=int(input("enter quantity"))
    d[key]=value
s=sum(d.values())
print(d)
print("quantity of product ", s)