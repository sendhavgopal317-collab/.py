r1=int(input("enter row of first matrics"))
c1=int(input("eneter column of first matics"))
r2=int(input("enter row of second matrics"))
c2=int(input("eneter column of second matics"))
a=[]
b=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input("enter elements of first matrics")))
    a.append(row)
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input("enter second elements ")))
    b.append(row)
if c1!=r2:
    print("solution not possible ")
else:
    result=[]
    for i in range(r1):
      row=[]
      for j in range(c2):
          row.append(0)
      result.append(row)
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j]=result[i][j]+a[i][k]*b[k][j]
print(result)
for row in result:
    print(*row)
