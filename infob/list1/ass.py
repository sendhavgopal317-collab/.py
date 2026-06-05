n=int(input("enter size"))
above=75
arr=[]
larg=0

for i in range(n):
    arr.append(int(input()))
low=arr[0]
count=0
for i in range(n):
    if arr[i]<low:
        low=arr[i]
    elif arr[i]>larg:
        larg=arr[i]
    if arr[i]>above:
        count=count+1
print("lowest number is ",low)
print("list is ",arr)

print("largest number is ",larg) 
print("count of num above 75",count)   