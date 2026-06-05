emp=int(input("enter  number of employee "))
month=int(input("enter no.of month "))
arrm=[]
for i in range(emp):
    row=[]
    for j in range(month):
        row.append(int(input("enter score -")))
    arrm.append(row)
while True:
    print("1. find employee with highest score ")
    print("2.find month with lowest average ")
    print("3. find month with max average score")
    print("4.exit")
    choice=int(input("enter your work"))
    match choice:
     case 3:
      for i in range(emp):
         highest=arrm[i][1]
         for j in range(month):
            if arrm[i][j]>highest:
               highest=arrm[i][j]
         print("emp ", j, "  month highest score" , highest)
     case 2:
          for i in range(month):
                      sum=0
                      low=(max(arrm[i]))*emp
                      print(low)
                      for j in range(emp):
                         sum=sum+arrm[i][j]
                      av=sum/j
                      if low>av:
                          low==av
                      print("average of month ", i , "is ", av)
     case 1:
            
      for i in range(emp):
         highest=0
         sum=0
         for j in range(month):
            sum=sum+arrm[i][j]
         if sum>highest:
               highest=sum
         print("emp ", j, "  month highest score" , highest)
     case 4:
            print("tq for using matrics operation ")
            break

       