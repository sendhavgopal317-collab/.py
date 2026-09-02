'''.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System'''
s={
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
while True:
    print("=========================================")
    print("        STUDENT MANAGEMENT SYSTEM        ")
    print("=========================================")

    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")
    choice=(input("enter you choice"))
    if choice not in "1234567890":
         print("enter valid choice")
    match choice:
         case "1":
              s_id=int(input("enter student id "))
              if s_id in s:
                   print("student already exist")
              else:
                   
                  
                  name=input("enter student name")
                  course=input("enter course")
                  mobile=input("enter mobile number")
                  fees=input("enter fee")
                  city=input("enter city")
                  s[s_id]={"student_id":s_id,
                                 "name":name,
                                 "course":course,
                                 "mobile":mobile,
                                 "fees":fees,
                                 "city":city}
         case "2":
              
           student_id = int(input("Enter Patient ID: "))

           if student_id in s:

            s = s[student_id]

            print("student ID :", student_id)
            print("Name       :", s["name"])
            print("course      :", s["course"])
            print("mobile num     :", s["mobile"])
            print("fees   :", s["fees"])
            print("city   :", s["city"])

           else:
            print("Patient Record Not Found")
         case "3":
            s_id=input("enter student id")
            if s_id not in s:
                print("student not found ")
            else:
                c=input("enter couse to update ")
                s[s_id][course]=c
                print("course updated succesfully")
         case "4":
            s_id=input("enter id of student")
            if s_id not in s:
                print("student not found ")
            else:
                del s[s_id]
                print("deleted succesfully")
         case "5":
            for i in s:
                print(s[i])
         case "6":
            c=0
            for i in s:
                c=c+1
            print("Total students are ", c)
         case "7":
            c=input("enter course")
            for i in s:

                if (s[i]["course"])==c:
                    print(s[i])
                else:
                    print("course not in syllabus")
         case "8":
            c=input("enter course")
            for i in s:
                if s[i]["city"]==c:
                    print(s[i])
                else:
                    print("no student from this city")
         case "9":
            l=0
            for i in s:
                if s[i]["fees"]>l:
                    l==s[i]["fees"]
                    student=s[i]["name"]
                    print(s[i]["fees"])

            print("student with highest fees",student)
         case "10":
            l=float("inf")
            for i in s:
                if s[i]["fees"]<l:
                    l==s[i]["fees"]
                    student=s[i]["name"]

            print("student with lowest fees",student)
         case "11":
            print("Exit done ")
            break
    print("want to contionue y/n")
    r=input("enter ").lower()
    if r=="y":
      continue
    else:
        break       


                                      
                