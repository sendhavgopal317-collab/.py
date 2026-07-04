"""12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680"""

b = int(input("Enter the Bill:"))
if b <= 1000 :
	f = b+(b*0.05)
	print("Final with GST :",f)
elif 1000 < b <= 5000:
	f = b+(b*0.12)
	print("Final with GST :",f)
else:
    print("Final with GST :",b+(b*0.18))
if 3000 < b:
	f = b+(b*0.12)
	print("Final with Service Charge:",f+200)