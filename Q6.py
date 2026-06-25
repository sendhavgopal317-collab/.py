"""6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000"""

sal = int(input("Enter the Salary:"))
exp = int(input("Enter the Experience:"))

if exp > 10 :
	print("Bonus Amount:",sal*0.2)
elif 10 >= exp >= 5:
	print("Bonus Amount:",sal*o.1)
elif 5 >= exp >= 2:
	print("Bonus Amount:",sal*0.05)
else:
	print("No Bonus")
