n=int(input("enter number :-"))
while n>0:
    if n%10==0:
        print("duck num")
        break
    n=n//10
else:
    print("non duck")   