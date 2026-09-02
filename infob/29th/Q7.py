"""7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000"""

amt = int(input("Enter the Withrawal Amount:"))
if amt < 1000 :
	print("Withrawal Not Allowed")
elif 1000 <= amt <= 5000:
	print("Maximum Withrawal 1000")
elif amt > 5000:
	print("Maximum withdrawal")