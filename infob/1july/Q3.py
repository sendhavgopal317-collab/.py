'''smart banking system'''
account_balance =0
intrest= 0
while True:
    print("1 :- deposite money")
    print("2 :- withdrawal money")
    print("3 :- check balance")
    print("4 :- apply intrest")
    print("5 :- exit")
    choice=int(input("what do you want tocheck"))
    match choice:
        case 1:
           n=int(input("enter money to deposite"))
           account_balance=n
           print("account balance updated successfully")     
        case 2:
           x=int(input("enter withdrawal amount"))
           if x<account_balance:
                print("withrdrawal done")
    
                print("remaining amount :-",account_balance-x)
                account_balance=account_balance-x
        case 3:
              print("current balance :-" , account_balance)
        case 4:
              if account_balance>50000:
                    intrest=(account_balance*5)/100
                    print(intrest)
              else:
                intrest=(account_balance*3)/100
                print(intrest)
                account_balance=account_balance+intrest
                current=("current balance",account_balance+intrest)
        case 5:
            print("exit")
            break
    choose=input("do you want to go ahead (yes/no)").lower()
    match choose:
        case "yes":
            continue
        case "no":
            print("exit")
            break
        case __:
            print("enter valid command ")



















