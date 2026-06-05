n=int(input("enter the size"))
arr=[]
polindrom=[]
non_p=[]
for i in range(n):
    arr.append(int(input()))
for i in range(n):

 rev=0
 temp=arr[i]
 while arr[i]>0:
    d=arr[i]%10
    rev=rev*10+d
    arr[i]=arr[i]//10
 if rev==temp:
    polindrom.append(rev)
 else: 
    non_p.append(rev)
print("polindrom no. are ",polindrom)
print("non polindrom no. are ",non_p)

       


    