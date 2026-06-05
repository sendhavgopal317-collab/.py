a=[[1,2],[3,4],[5,6]]
print(a)
'''
print(a[0][1])
for i in a:
    print(i)
    for j in i:
        print (j,end=" ")
    print()'''
for i in range (len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()