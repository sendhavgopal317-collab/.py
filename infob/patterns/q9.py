n=int(input("enter"))
i=n
while i>=1:
    ch=65
    j=1
    while j<=i:
        if i%3==0:
            ch=ch-3
            print(chr(ch),end="")
            ch=ch+3
        else:
         print(chr(ch) , end="")
        j=j+1
        ch=ch+1
    print()
    i=i-1