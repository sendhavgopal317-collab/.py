r1=int(input("enetr row size of first "))
c1=int(input("enter col for 1 matrics "))
r2=int(input("enetr row size of secomd "))
c2=int(input("enter col for 2 matrics "))
A=[]
B=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input("elements ")))
    A.append(row)
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input("elements ")))
    B.append(row)
while True:
    print("1.Add two matrics")
    print("2.subtract two matrices")
    print("3.compare two matrices")
    print("4.exit")
    choice=int(input("enter your choice"))
    if r1!=r2 and c1!=c2:
        print("operations not available ")
    else:
     match choice:
        case 1:
            s=[]
            for i in range (len(A)):
               row=[]
               for j in range (len(A[i])):
                 row.append(A[i][j]+B[i][j])
               s.append(row)
            print("sum of matric is ",s)
        case 2:
            s=[]
            for i in range (len(A)):
               row=[]
               for j in range (len(A[i])):
                 row.append(A[i][j]-B[i][j])
               s.append(row)
            print("sum of matric is ",s)
        case 3:
                    s=[]
                    for i in range (len(A)):
                       m=True
                       row=[]
                       for j in range (len(A[i-1])):
                           if (A[i][j]!=B[i][j]):
                               m=False
                               print("matrics are not equal")
                               break
                           row.append(m)
                       else:
                           print("matrics are equal")
                       s.append(row)
                    for row in s:
                        print(*row)
        case 4:
             print("exited")
             break
        


