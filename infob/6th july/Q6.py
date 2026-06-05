n = int(input("Enter number: "))

original = n

# Reverse the number
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

# Square of original and reversed numbers
sqr = original ** 2
sq2 = rev ** 2

# Reverse the square of the reversed number
square_reverse = 0
while sq2 > 0:
    digit = sq2 % 10
    square_reverse = square_reverse * 10 + digit
    sq2 = sq2 // 10

print("Square of original:", sqr)
print("Reverse of square of reverse:", square_reverse)

if sqr == square_reverse:
    print("Adam number")
else:
    print("Not an Adam number")