import math
n=int(input("enter size"))
arr=[]
prime=[]
count=0
count2=0
non_prime=[]
largest=0
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    if (arr[i])<2:
        non_prime.append(arr[i])

    else:
        for j in range(2,arr[i]):
            if arr[i]%j==0:
                non_prime.append(arr[i])
                break
        else:
            prime.append(arr[i])
    
print("prime no.",sorted(prime), "count of prime", count)
print("non prime", sorted(non_prime) ,"count of non prime", count2)
