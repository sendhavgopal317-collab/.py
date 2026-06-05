n=int(input("enter number of employees "))
k=int(input("enter difference"))
arr=[]
for i in range(n):
    arr.append(int(input("enter age of employees")))
count=0
for i in range(0,n):
    for j in range(0,n):
        if arr[i]-arr[j]==k:
            count=count+1
            c=(arr[i],arr[j])
            print(c)
            print(type(c))
print("count of k in n is ", count)

    
