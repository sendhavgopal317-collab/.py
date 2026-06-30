'''read trvell kilometers'''
n=int(input("enter travel km  : "))
t=3000
if n<3000:
    print("bike service on 3000km")
else:
    i=t
    while n>i:
        print(i)
        i=i+t

