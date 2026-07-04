"""1.Insurance Claim Approval System
An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation"""

p = int(input("Enter the Policy Age:"))
c = float(input("enter the Claim Amount:"))
a = input("Accident type(major/minor) :")

if p >= 2:
   if c <= 50000:
       if a == "minor":
          print("Approve the claim")
       else:
          print("Approve it with Inspection")
   elif 50000 < c < 200000:
      if a == "major":
          print("approve with investigation")
      else:
          print("Reject")
   else:
      print("Reject")
elif a == "minor":
    print("Reject")
else:
    print("Pending Review")