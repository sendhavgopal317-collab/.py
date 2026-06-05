# Matrix Multiplication

r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible")

else:
    A = []
    B = []

    print("Enter first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    C = []

    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0

            for k in range(c1):
                sum = sum + A[i][k] * B[k][j]

            row.append(sum)

        C.append(row)

    print("Result:")
    for i in range(r1):
        for j in range(c2):
            print(C[i][j], end=" ")
        print()