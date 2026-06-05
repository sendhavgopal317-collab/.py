from collections import namedtuple
employee=namedtuple("emp",["emp_id","emp_name","department","salary"])
k=int(input("enter number of employees "))
employees=[]
for i in range(k):
    id=input("enter id ")
    n=input("enter name ")
    d=input("enter depa- ")
    sal=int(input("enter salary"))
    s=employee(id,n,d,sal)
    employees.append(s)

for x in employees:
   print(x.emp_id,x.emp_name,x.department,x.salary)
high=0
low=float('inf')
sum=0
for i in employees:
    if (i.salary)>high:
        sum+=i.salary
        high=i.salary
        emph=(i.emp_id,i.emp_name,i.department,i.salary)
    if i.salary<low:
        low=i.salary
        empl=(i.emp_id,i.emp_name,i.department,i.salary)
dep=input("enter department")
for x in employees:
 if x.department==dep:
    print(x.emp_id,x.emp_name,x.department,x.salary)
print("highest salary",emph)
print("lowest salary",empl)
av=sum/k
print("average is ",av)


   
