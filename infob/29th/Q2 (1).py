"""2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C"""

m = int(input("Enter the marks:"))
if m >= 90:
	print("Grade A")
elif 89>= m  >=75:
	print("Grade B")
elif 74>= m >=60:
	print("Grade C")
elif 59>= m >=50:
	print("Grade D")
else:
	print("Fail")


