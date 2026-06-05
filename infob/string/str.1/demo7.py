n=input("enter vehicle number ").upper()
i=0
if len(n)!=10 or n[0]<'A' or n[0]>'Z' or  n[1]<'A' or n[1]>'Z' or  n[2]not in'1234567890'  or n[3]not in'1234567890' or  n[4]<'A' or n[4]>'z' or  n[5]<'A' or n[5]>'Z' or  n[6]not in'1234567890' or n[7]not in'1234567890' or n[8]not in'1234567890' or n[9]not in'1234567890'   :
    print("invalide vehicle num.")
else:
    print(":  valid number  :")
    print("vehicle num is:-",n)