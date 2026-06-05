# write a program to print some of diagonal ::::
m=[[1,3,4],[6,7,8],[2,5,9]]
dsum=0
for i in range(len(m)):
    dsum=dsum+m[i][i]
print ("diagonal sum is ",dsum)