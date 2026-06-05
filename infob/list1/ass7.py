n=int(input("enter the of hikings "))
arr=[]
top=[]
sum=0
product=1
largest=0
for i in range(n):
    arr.append(int(input("enter elevation ")))
if len(arr)<2:
    top.append(arr[0])
    print(top)
else:
    for i in range(n):
        i=1
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
           sum=sum+arr[i]
           product=product*arr[i]
           if largest<arr[i]:
              largest=arr[i]
         
if arr[n-1]>arr[n-2]:

 print(arr[n-1])
print("product is ",product )
print("sum is ", sum)
print("largest is ", largest)