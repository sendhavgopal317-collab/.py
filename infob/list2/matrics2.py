r1=int(input("enetr row size of first "))
c1=int(input("enter col for 1 matrics "))
A=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input("elements ")))
    A.append(row)
while True:
    print("1.count prime number row wise ")
    print("2.count prime number column wise ")
    print("3.display rowise sum ")
    print("4.exit ")
    choice=int(input("enter your choice "))
    match choice:
        case 1:
            for i in range(r1):
                for j in range(c1):
                  num=A[i][j]
                  if num<2:
                      print(i,num," not prime")
                  else:
                   for k in range(2,num): 
                    if num%k==0:
                       print(i," ", num , " not prime ")
                       break
                   else:
                      print(i," ", num , "  prime ")
        case 2:
          for i in range(c1):
             count=0
             for j in range(r1):
                num=A[i][j]
                sum=0
                for k in range(1,num):
                   if num%k==0:
                      sum=sum+k
                if sum==num:
                   count=count+1
             print("column", i ," perfect number is" ,count )
        case 3:
          for i in range(r1):
             sum=0
             for j in range(c1):
                num=A[i][j]
                sum=sum+num
             print("sum of ", i, " row is ",sum)
        case 4:
          print("Thank you for using matrics analysis ")
          break
                

                      
                              
                      
