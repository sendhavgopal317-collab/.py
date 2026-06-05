k=int(input("enter size"))
arr=[]
for i in range(k):
    arr.append(int(input("enter elements")))
result=""
pos=[]
neg=[]
x=[]
for i in range(k):
  if arr[i]>0:
     pos.append(arr[i])
  else:
     neg.append(arr[i])
l=min(len(pos),len(neg))

for i in range(l):
   x.append(pos[i])
   x.append(neg[i])
if len(pos)>len(neg):
   for i in range(len(neg),len(pos)):
      x.append(pos[i])
if len(neg)>len(pos):
   for i in range(len(pos),len(neg)):
      x.append(neg[i])
print(x)
