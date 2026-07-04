n=int(input("numb"))
sum=0
i=1
for i in range (1, n//2+1):
    if n %i ==0:
        sum = sum+1
if sum==n:
    print ("perfect")
else:
    print("not ")            