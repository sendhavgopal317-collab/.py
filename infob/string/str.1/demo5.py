n=input("enter your password:-")
lower=0
special=0
digit=0
space=0
i=0
if len(n)<8 or len(n)>15 or n[-1]not in"1234567890" or n[0]<'A' or n[0]>'Z':
    print("insecure password")
else:
 while i<len(n):
    ch=n[i]
    if ch in '1234567890':
       digit=digit+1
    elif ch>='a' and ch<='z':
       lower=1
    elif ch == " ":
       space=1
    elif ch>='A' and ch<='Z':
       pass
    else :
       print(ch)
       special=1
    i=i+1
 if  lower==1 and  digit>1 and special==1 and space==0:
      print("strong password ")
 else :
      print("week password")
