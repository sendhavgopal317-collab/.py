n=int(input("enter number"))
count=0
while n>=0:
    digit=n%10
    n=n//10
    temp=n//10
    while temp>=0:
        digit2=temp%10 
        temp=temp//10
        if digit==digit2:
            print("rejected")
            count=count+1
            break
    if count>=1:
         break
else:
    if count ==0:
        print("accept")