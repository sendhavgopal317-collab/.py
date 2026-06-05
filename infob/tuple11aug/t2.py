n=int(input("enter string"))
arr=[]
for i in range  (n):
    arr.append(input())
count=0
for i in range(len(arr)):
    for j in range(i,n):
        for ch in arr[i]:
            if ch in arr[j]:
                break
        else:
         count+=1
         print(arr[i],arr[j])
print(count)
