n = int(input("Enter the size of matrix: "))

matrix = []

print("\nEnter matrix elements:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nOriginal Matrix:")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

print("\nMain Diagonal Elements:")

for i in range(n):
    print(matrix[i][i], end=" ")
print()

print("\nSecondary Diagonal Elements:")

for i in range(n):
    print(matrix[i][n - 1 - i], end=" ")
print()

transpose = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    transpose.append(row)

print("\nTranspose Matrix:")

for i in range(n):
    for j in range(n):
        print(transpose[i][j], end=" ")
    print()


for i in range(n):
    j = n - 1 - i

    temp = transpose[i][i]
    transpose[i][i] = transpose[i][j]
    transpose[i][j] = temp

print("\nFinal Matrix After Diagonal Swapping:")

for i in range(n):
    for j in range(n):
        print(transpose[i][j], end=" ")
    print()
