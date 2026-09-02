classes=int(input("enter the number of classes : "))
students=int(input("enter num of students : "))
subjects=int(input("enter num of subjects : "))
sum=0
i=1
n=1
m=1
for i in range(1,classes+1):
    for n in range(1,students+1):
        for m in range(1,subjects+1):
            s=int(input("marks :- "))
            sum=sum+s
        print("class :", i)
        print("student :", n)
        print("total ", sum)