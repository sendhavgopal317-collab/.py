'''Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days

'''
from datetime import datetime, timedelta

dob = input("Enter DOB (DD-MM-YYYY): ")
dob = datetime.strptime(dob, "%d-%m-%Y")
today = datetime.now()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print("Age:", age, "years")
total_days_lived = (today - dob).days
print("Total Days Lived:", total_days_lived, "days")
next_birthday = dob.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
print("Next Birthday:", next_birthday.strftime("%d-%m-%Y"))
days_remaining = (next_birthday - today).days
print("Days Remaining:", days_remaining, "days")