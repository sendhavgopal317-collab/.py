"""2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted"""\

m = int(input("Enter the marks :"))
s = int(input("enter the EntranceScore :"))
c = input("Enter the Category(general/obc/st-sc):")

if m >= 70:
   if s >= 80:
      if c == "general":
          print("Admit")
      else:
          print("Admit with Scholarship")
   elif s <80:
      if m>= 85:
          print("Admit Under Management Quota")
      else:
          print("Reject")
elif m < 70 :
      if c != "general" and m >= 60:
         if s <= 70:
             print("Waitlist")
         else:
             print("Reject")
else:
    print("Reject")
         