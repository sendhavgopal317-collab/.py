'''Assignment: Menu-Driven Number Analysis System

Create a Menu-Driven Number Analysis System in Python.

The program should continuously display a menu and allow the user to select different operations related to numbers.

Each operation must be implemented using a separate function.

The program should continue running until the user selects Exit.

Main Menu

When the program starts, display:

========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit

Enter your choice:

The program must ask for the required input only after the user selects an operation.

CASE 1: Perfect Number
Function

Create:

def is_perfect(number):
What to read from the user?

Read:

Enter a number:
Requirement

Check whether the given number is a Perfect Number.

A number is perfect if the sum of its proper divisors is equal to the number itself.

Example:

6

Proper divisors:

1 + 2 + 3 = 6

Therefore:

6 is a Perfect Number
Sample Output
Enter a number: 6

6 is a Perfect Number

For:

Enter a number: 10

10 is not a Perfect Number
CASE 2: Palindrome Number
Function

Create:

def is_palindrome(number):
What to read from the user?
Enter a number:
Requirement

Check whether the number reads the same from both directions.

Example:

121

Reverse:

121

Therefore:

121 is a Palindrome Number
Sample Output
Enter a number: 121

121 is a Palindrome Number
CASE 3: Strong Number
Function

Create:

def is_strong(number):
What to read from the user?
Enter a number:
Requirement

A number is a Strong Number if the sum of the factorials of its digits is equal to the original number.

Example:

145

Calculation:

1! + 4! + 5!

1 + 24 + 120

= 145

Therefore:

145 is a Strong Number
Sample Output
Enter a number: 145

145 is a Strong Number
CASE 4: Armstrong Number
Function

Create:

def is_armstrong(number):
What to read from the user?
Enter a number:
Requirement

Check whether the given number is an Armstrong Number.

For a 3-digit number:

153

Calculation:

1³ + 5³ + 3³

1 + 125 + 27

= 153

Therefore:

153 is an Armstrong Number
Sample Output
Enter a number: 153

153 is an Armstrong Number
Important

Do not hard-code the number of digits.

The function should work for numbers having different numbers of digits.

CASE 5: Prime Number
Function

Create:

def is_prime(number):
What to read from the user?
Enter a number:
Requirement

Check whether the given number is prime.

A prime number has exactly two factors:

1 and itself

Example:

17

Factors:

1, 17

Therefore:

17 is a Prime Number
Sample Output
Enter a number: 17

17 is a Prime Number
CASE 6: Even or Odd
Function

Create:

def check_even_odd(number):
Input
Enter a number:
Requirement

Determine whether the number is:

Even

or

Odd
Example
Enter a number: 24

24 is an Even Number
CASE 7: Factorial
Function

Create:

def factorial(number):
Input
Enter a number:
Requirement

Find the factorial of the given number.

Example:

5! = 5 × 4 × 3 × 2 × 1
   = 120
Output
Enter a number: 5

Factorial = 120
CASE 8: Sum of Digits
Function

Create:

def sum_of_digits(number):
Input
Enter a number:
Requirement

Calculate the sum of all digits.

Example:

Enter a number: 5832

5 + 8 + 3 + 2 = 18
Output
Sum of digits = 18
CASE 9: Reverse a Number
Function

Create:

def reverse_number(number):
Input
Enter a number:
Requirement

Reverse the given number.

Example:

Enter a number: 12345

Reverse = 54321
CASE 10: Count Number of Digits
Function

Create:

def count_digits(number):
Input
Enter a number:
Requirement

Find how many digits are present in the number.

Example:

Enter a number: 98765

Number of digits = 5
CASE 11: Automorphic Number
Function

Create:

def is_automorphic(number):
Input
Enter a number:
Requirement

A number is Automorphic if its square ends with the same number.

Example:

25² = 625

625 ends with:

25

Therefore:

25 is an Automorphic Number
Output
Enter a number: 25

25 is an Automorphic Number
CASE 12: Neon Number
Function

Create:

def is_neon(number):
Input
Enter a number:
Requirement

A number is Neon if the sum of the digits of its square is equal to the original number.

Example:

9² = 81

8 + 1 = 9

Therefore:

9 is a Neon Number
Output
Enter a number: 9

9 is a Neon Number
CASE 13: Spy Number
Function

Create:

def is_spy(number):
Input
Enter a number:
Requirement

A number is a Spy Number if:

Sum of digits = Product of digits

Example:

1124

Sum:

1 + 1 + 2 + 4 = 8

Product:

1 × 1 × 2 × 4 = 8

Therefore:

1124 is a Spy Number
CASE 14: Harshad Number
Function

Create:

def is_harshad(number):
Input
Enter a number:
Requirement

A number is a Harshad Number if it is completely divisible by the sum of its digits.

Example:

18

Sum of digits:

1 + 8 = 9

Check:

18 % 9 == 0

Therefore:

18 is a Harshad Number
CASE 15: Exit

When the user selects:

15

Display:

Thank you for using Number Analysis System!
Program terminated.

Then terminate the program.

Important Programming Requirements

Students must follow all of these rules.

1. Separate Function for Every Operation

Do not write all logic directly inside the menu.

For example:

def is_prime(number):
    # logic
def is_palindrome(number):
    # logic
def factorial(number):
    # logic
2. Functions Must Receive Input Through Parameters

Correct:

def is_prime(number):

Incorrect:

def is_prime():
    number = int(input("Enter number: "))

For this assignment, the main program should read the input and pass it to the function.

3. Functions Should Return Results

For example:

result = is_prime(number)

Then use:

if result:
    print("Prime Number")
else:
    print("Not Prime Number")
4. Menu Must Run Continuously

Use:

while True:

The menu should appear again after every operation.

Example:

1. Perfect
2. Palindrome
3. Strong
...
15. Exit

Enter choice: 1

Enter number: 6

6 is a Perfect Number


========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Perfect
2. Palindrome
...
5. Invalid Choice

If the user enters:

20

Display:

Invalid Choice!
Please select a choice between 1 and 15.

Then display the menu again.

6. Input Should Be Taken According to the Selected Case

For example, if the user selects:

1

then:

Enter a number:

should be displayed.

Do not take input for all 14 operations at the beginning.

Expected Program Flow
========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit

Enter your choice: 4

Enter a number: 153

153 is an Armstrong Number

----------------------------------------

Press Enter to continue...

========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit

Enter your choice: 15

Thank you for using Number Analysis System!
Program terminated.'''

from tokenize import Number
def is_perfect(number):
    if number < 1:
        return False
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_of_divisors == number
def is_palindrome(number):
    return str(number) == str(number)[::-1]
def is_strong(number):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
    return sum_of_factorials == number
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
def factorial(number):
    if number < 0:
        return None
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
def reverse_number(number):
    return int(str(abs(number))[::-1]) * (-1 if number < 0 else 1)
def count_digits(number):
    return len(str(abs(number)))
def is_automorphic(number):
    square = number ** 2
    return str(square).endswith(str(number))
def is_neon(number):
    square = number ** 2
    return sum(int(digit) for digit in str(square)) == number
def is_spy(number):
    digits = [int(digit) for digit in str(abs(number))]
    return sum(digits) == (1 if not digits else eval('*'.join(map(str, digits))))
def is_harshad(number):
    if number == 0:
        return False
    digit_sum = sum(int(digit) for digit in str(abs(number)))
    return number % digit_sum == 0
number=int(input("Enter a number: "))


while True:
    print("="*40)
    print("       NUMBER ANALYSIS SYSTEM")
    print("="*40)
    print("1. Check Perfect Number")
    print("2. Check Palindrome Number")
    print("3. Check Strong Number")
    print("4. Check Armstrong Number")
    print("5. Check Prime Number")
    print("6. Check Even or Odd")
    print("7. Find Factorial")
    print("8. Find Sum of Digits")
    print("9. Reverse a Number")
    print("10. Find Number of Digits")
    print("11. Check Automorphic Number")
    print("12. Check Neon Number")
    print("13. Check Spy Number")
    print("14. Check Harshad Number")
    print("15. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            if is_perfect(number):
                print(f"{number} is a Perfect Number")
            else:
                print(f"{number} is not a Perfect Number")
        case "2":
            if is_palindrome(number):
                print(f"{number} is a Palindrome Number")
            else:
                print(f"{number} is not a Palindrome Number")
        case "3":
            if is_strong(number):
                print(f"{number} is a Strong Number")
            else:
                print(f"{number} is not a Strong Number")
        case "4":
            if is_armstrong(number):
                print(f"{number} is an Armstrong Number")
            else:
                print(f"{number} is not an Armstrong Number")
        case "5":
            if is_prime(number):
                print(f"{number} is a Prime Number")
            else:
                print(f"{number} is not a Prime Number")
        case "6":
            result = check_even_odd(number)
            print(f"{number} is an {result} Number")
        case "7":
            result = factorial(number)
            if result is not None:
                print(f"Factorial = {result}")
            else:
                print("Factorial is not defined for negative numbers.")
        case "8":
            result = sum_of_digits(number)
            print(f"Sum of digits = {result}")
        case "9":
            result = reverse_number(number)
            print(f"Reverse = {result}")
        case "10":
            result = count_digits(number)
            print(f"Number of digits = {result}")
        case "11":
            if is_automorphic(number):
                print(f"{number} is an Automorphic Number")
            else:
                print(f"{number} is not an Automorphic Number")
        case "12":
            if is_neon(number):
                print(f"{number} is a Neon Number")
            else:
                print(f"{number} is not a Neon Number")
        case "13":
            if is_spy(number):
                print(f"{number} is a Spy Number")
            else:
                print(f"{number} is not a Spy Number")
        case "14":
            if is_harshad(number):
                print(f"{number} is a Harshad Number")
            else:
                print(f"{number} is not a Harshad Number")
        case "15":
            print("Thank you for using Number Analysis System!")
            print("Program terminated.")
            break
        case _:
            print("Invalid Choice!")
