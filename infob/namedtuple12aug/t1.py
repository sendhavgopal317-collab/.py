from collections import namedtuple
students=namedtuple("std",["name", "rollno","marks"])
n=int(input("enter the number of students"))
student=[]
for i in range(n):
    print("enter details ")
    name=input("enter name ")
    roll=int(input("enter rollnum. "))
    mark=float(input("enter marks "))
    s=students(name,roll,mark)
    student.append(s)
for x in student:
    print(x.name,"and",x.rollno,"and ", x.marks)
