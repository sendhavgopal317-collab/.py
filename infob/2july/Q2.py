a=int(input("enter number "))
b=int(input("enter second number  "))
for n in range(a,b+1):
        for i in range(2, n//2+1):
            if n%i==0:
                break
        else:
            if n<2:
                 continue
            else:
             print(n)