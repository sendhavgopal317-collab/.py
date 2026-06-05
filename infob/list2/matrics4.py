'''
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
'''

print("=========================================================")
print("        MATRIX DIAGONAL ANALYSIS SYSTEM                  ")
print("=========================================================")
while True:
   print("1. Display Main Diagonal Elements")
   print("2. Display Secondary Diagonal Elements")
   print("3. Compare Main and Secondary Diagonal Sums")
   print("4. Exit")
   choice=int(input("Enter your choice :"))
   match choice:
       case 1:
            r1=int(input("Enter number of rows :"))
            c1=int(input("Enter number of column :"))
            matrix=[]
            for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix.append(row)
            #print(matrix)
            for i in range(len(matrix)):
                print(matrix[i][i],end=" ")    
            print()
       case 2:
            r1=int(input("Enter number of rows :"))
            c1=int(input("Enter number of column :"))
            matrix=[]
            for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix.append(row)
            #print(matrix)
            j=c1-1
            for i in range(len(matrix)):
                while j>=0:
                    print(matrix[i][j],end="")
                    break
                j-=1
            print()
       case 3:
            r1=int(input("Enter number of rows :"))
            c1=int(input("Enter number of column :"))
            matrix=[]
            for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix.append(row)
            #print(matrix)
            dsum=0
            for i in range(len(matrix)):
                print(matrix[i][i],end=" ")
                dsum+=matrix[i][i]    
            print()
            j=c1-1
            dsum1=0
            for i in range(len(matrix)):
                while j>=0:
                    print(matrix[i][j],end=" ")
                    dsum1+=matrix[i][j]
                    break
                j-=1
            print()
            print("main diagonal sum :",dsum)
            print("secondary diagonal sum :",dsum1)
            print()
            if dsum==dsum1:
                print("Both Diagonal Sums are Equal")
            else:
                print("Both Diagonal Sums are not  Equal")
            print()

       case 4:
             print("Thank You for Using Matrix Diagonal Analysis System")  
             break                  
                    
                    
                 
                 
                                
