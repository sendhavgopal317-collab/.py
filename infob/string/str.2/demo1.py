n=input("enter username ").lower()
i=0
if n[0]<'a' or n[0]>'z' or len(n)<5 or len(n)>12:
    print("invalid username")
else:
    while i<len(n):
        ch=n[i]
        if ch  in " ":
            print("invalid username ")
            break
        elif ch in "_":
            pass
        elif ch in "1234567890":
         pass
        elif ch<'Z' and ch>'A':
            pass
        elif ch>'a'and ch<'z':
            pass
        else:
            print("invalid username . ")
            break
        i=i+1
    else:
        print(n," is valid username " )
