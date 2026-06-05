n=int(input("enter"))
i=1
while i<=n:
    ch=65
    j=1
    while j<=i:
        print(chr(ch) , end="")
        j=j+1
        ch=ch+1
    print()
    i=i+1