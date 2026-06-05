n=int(input("entr size"))
k=int(input("enter the target sum"))
arr=[]
for i in range(n):
    arr.append(int(input()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            count=count+1
            print(i,i+j)
print("count is ",count)