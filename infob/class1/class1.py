m=[[1,3,4],[6,7,8],[2,5,9]]
count=0
for row in m:
    for val in row:
        if val%2==0:
         count+=1
print("count of even numbers",count)