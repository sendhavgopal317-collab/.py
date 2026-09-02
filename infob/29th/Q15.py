"""15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220"""

v = input("Enter the vehicle type:")
h = int(input("Enter your Parking hours:"))
if v == "bike":
	p = 10*h
	print("As ₹10/hour :",p)
elif v == "car":
	p = 20*h
	print("As ₹20/hour :",p)
elif v == "bus":
	p = 50*h
	print("As ₹50/hour :",p)
else:
	print("No Parking")
if h >= 5:
        print("Final with Additional charge:", p+100)
else:
    print("No Additional Charge")



