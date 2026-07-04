"""11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600"""

d = int(input("Enter the Distance :"))
c = input("Enter the Class(Sleeper/AC):")
if d <= 100:
	print("Sleeper = 100rs, AC = 200rs")
elif 101 <= d <= 500:
	print("Sleeper = 300rs, AC = 600rs")
else:
	print("Sleeper = 500rs, AC = 1000rs")