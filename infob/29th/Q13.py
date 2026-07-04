"""13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600"""

s = int(input("Enter the Salary:"))
r = int(input("Enter the Ratings:"))
if r ==5:
	rs = s+(s*0.25)
	print("Revised Salary with 25% hike:",rs)
elif r ==4:
	rs = s+(s*0.20)
	print("Revised Salary with 20% hike:",rs)
elif r ==3:
	rs = s+(s*0.10)
	print("Revised Salary with 10% hike:",rs)
elif r ==2:
	rs = s+(s*0.05)
	print("Revised Salary with 5% hike:",rs)
else :
	
	print("No Hike")


