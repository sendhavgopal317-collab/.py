n=int(input("enter the of hikings "))
arr=[]
top=[]
for i in range(n):
    arr.append(int(input("enter elevation ")))
if len(arr)<2:
    top.append(arr[0])
else:
    for i in range(n):
        i=1
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
         print(i)
if arr[n-1]>arr[n-2]:

 print(arr[n-1])
