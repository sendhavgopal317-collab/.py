'''salary processor'''
salary=0
tax=0
allowance=0
net_salary=0
while True:
    print("1 :- enter basic salary")
    print("2:- calculate HRA (20%)and DA(10%)")
    print("3 :-calculate salary")
    print("4 :-tax deduction")
    print("5:- print salary slip")
    print("6:- exit")
    choice=int(input("enter what do you want to check"))
    match choice:
        case 1 :
            n=int(input("enter your basic salary"))
            print("basic salary recorded succesfully")
            salary=n
        case 2:
            if salary==0:
                print("please enter salary first")
            else:
                HR=(salary*20/(100))
                DA=(salary*10/(100))
                allowance=HR+DA
                print("HRA:-" , HR)
                print("DA :-",DA)
        case 3:
            if salary==0:
                print("enter salary first")
            else:
                HRA=(salary*20/(100))
                DA=salary*10/(100)
                net_salary=salary+HRA+DA
            print("net salary:-", salary+HRA+DA)
            print ("without tax")
        case 4:
            if net_salary==0:
                print("enter salary")
            else:
                if salary>50000:
                    tax=(net_salary*10)/100
                    print(tax)
                else:
                    tax=(net_salary*5)/100
                    print(tax)
        case 5:
            print("---salary slip---")
            print("basic salary :-", salary)
            print("HRA+DA :-", allowance)
            print("net salary :-", net_salary)
            print("tax :- ", tax)
            print("final salary:- " , net_salary-tax)
        case 6:
            print("exit:")
            break
        case __:
            print("invalid choice.please try again")
            break




        