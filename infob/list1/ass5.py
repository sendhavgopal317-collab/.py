n=int(input("enter survey size "))
arr=[]
counted=[]
invalid=[]
valid=[]
ln=0
hn=0
for i in range(n):
    arr.append(int(input("enter survey data ")))
highest=0
lowest=n
for i in range(n):
    count=0
    if arr[i]<=0:
         invalid.append(arr[i])
    else:
         valid.append(arr[i])
    if arr[i] not in counted and arr[i] in valid:
        j=i+1
        for j in range(n):
            if arr[i]==arr[j]:
                count=count+1
            counted.append(arr[i])
        print("count of ", arr[i],"=", count)
        if highest<count:
                highest=count
                hn=arr[i]
        if lowest>count:
                lowest=count
                ln=arr[i]
if highest==n:
 lowest=0
 print("lowest frequency is ",lowest)
else:
     print("lowest fresquency is",lowest)
print("highest frequency is ",highest)
if valid==[]:
     print("no valid count found ")
else:
     print("valid is ",valid)
print("invalid are",invalid)
print("highest frequancy is  of", hn)
print("lowest frequancy is  of", ln)
