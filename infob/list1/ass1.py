n=int(input("enter number of employee:-- "))
arr=[]
for i in range(n):
    arr.append(int(input()))
sum=0
above_average=[]
for i in range(n):
    sum=sum+arr[i]
average=sum/n
for i in range(n):
    if arr[i]>average:
        above_average.append(arr[i])
print("averagew is ", average)
print("salary above average is ", above_average)

