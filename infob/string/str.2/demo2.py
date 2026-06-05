n=input("enter your mobile number")
i=0 
count=0

while i<len(n):
    ch=n[i]
    if ch in "1234567890":
        count=count+1
    elif ch not in "123456790":
        count=count
    i=i+1
print('count is =', count)

