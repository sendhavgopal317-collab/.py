m=[[1,2,4],[6,7,8],[2,5,9]]
n=[[1,2,4],[6,7,8],[2,5,9]]
s=[]
for i in range (len(m)):
    row=[]
    for j in range (len(m[i])):
        row.append(m[i][j]+n[i][j])
    s.append(row)
print("sum of matric is ",s)
