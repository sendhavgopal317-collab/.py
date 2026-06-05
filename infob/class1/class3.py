m=[[1,2,4],[6,7,8],[2,5,9]]
s=int(input("enter search element "))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==s:
            print("element found at ", i,j )
