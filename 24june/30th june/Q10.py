
mode=int(input("enter mode of lift ; "))
if mode==1:
    floor=int(input("enter current floor : "))
    destination=int(input("enter destination floor :  "))
    for i in range(floor , destination+1):
        print(i, end ="")
elif mode==2:
    floor=int(input("enter current floor : "))
    destination=int(input("enter destination floor :  "))
    for i in range(floor , destination-1 , -1):
        print(i ,end="")
elif mode==3 :
    floor=int(input("enter current floor : "))
    destination=int(input("enter destination floor :  "))
    for i in range (0,destination+1 , +2):
        print(i ,end="")
else:
    for i in range(4):
     print("emergency alarm")
     