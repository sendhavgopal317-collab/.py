print("="*50)
print(" "*10," ROAD TRIP PLANNER ")
print("="*50)
print("Enter travel details :")
budget=int(input("enter your trip budget :--"))
number_of_people=int(input("enter number of people :--"))
total_distance=int(input("Enter one side distance "))
s=input("enter if you want to calculate return fair (yes/no)")
if s=="yes":
    total_distance=total_distance*2
elif s=="no":
    total_distance=total_distance
else:
    print("enter a valid input")
print("Enter vehicle details :")
milage=(int(input("Enter vehicle milage :")))
fuel_price=(int(input("Enter fuel price :")))
print("Hotel price by default is 500 per head ")
hotel_price=input("want to change hotel price(yes/no)").lower()
if hotel_price=="yes":
    hotel_price=(int(input("Enter price :-- ")))
elif hotel_price=="no":
    hotel_price=int(500)
else:
    print("enter valid input")
print("Taking food price RS=200/- by default :")
food_cost=(input("Want to change food cost(yes/no)")).lower()
if food_cost=="yes":
    food_cost=int(input("enter food cost per person :--"))
if food_cost=="no":
    food_cost=int(200)
else:
    print("enter valid input ")
toll_cost=(total_distance/50)*50
other_expense=int(input("enter per day expense :--"))
total_fuel=(total_distance/milage)
print("total fuel=",total_fuel)
fuel_cost=float(total_fuel*fuel_price)
total_food_cost=int(food_cost*number_of_people)
travel_per_day=100
total_days=float(total_distance/travel_per_day)
total_hotel_cost=float(hotel_price*number_of_people*total_days)
total_other_expense=float(total_days*other_expense)
total_trip_cost=float(total_food_cost+total_hotel_cost+total_other_expense+fuel_cost+toll_cost)
print("total food cost:--",total_food_cost)
print("total hotel expense:--",total_hotel_cost)
print("total fuel expense :--",fuel_cost)
print("Other expense :--", total_other_expense)
print("toll expense :--", toll_cost)
print("total trip expense:--", total_trip_cost)
if budget<total_trip_cost:
    print("Budget is less than trip cost ")
    print("You have  to reduce cost ")
    if fuel_cost>total_food_cost:
        if fuel_cost>total_hotel_cost:
            if fuel_cost>total_other_expense:
                print("Have to reduce fuel cost ")
                print("drive at average speed ")
                c=input("Want to explore other ways to travel(yes/no)")
                if c=="yes":
                    if total_distance<200:
                        print("should prefer bike ")
                    elif total_distance>600:
                        print("can prefer train ")
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input ")
            else:
                print("Too much other expense ")
                c=input("want to reduce other expense (yes/no)")
                if c=="yes":
                    print("use free parking space instaed of paid ")
                    print("if using cash for toll payment than reduce it by fastage ") 
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input")
        else:
            if total_hotel_cost>total_other_expense:
                print("You have to reduce hotel cost")
                c=input("want to reduce hotel expense (yes/no)")
                if c=="yes":
                    print("stay local hotel ")
                    print("go for budget friendly hotels") 
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input")
            else:
                print("Too much other expense ")
                c=input("want to reduce other expense (yes/no)")
                if c=="yes":
                    print("use free parking space instaed of paid ")
                    print("if using cash for toll payment than reduce it by fastage ") 
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input")
    else:
        if total_food_cost>total_hotel_cost:
            print("food budget is is high ")
            c=input("if you want to reduce food cost(yes/no)")
            if c=="yes":
                print("use local restaurants /carry snaks /avoid expensive cafe")
            elif c=="no":
                   print(total_trip_cost-budget+(total_trip_cost-budget))
            else:
                print("enter valid input")
        elif total_hotel_cost>total_other_expense:
                print("You have to reduce hotel cost")
                c=input("want to reduce hotel expense (yes/no)")
                if c=="yes":
                    print("stay local hotel ")
                    print("go for budget friendly hotels") 
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input") 
        else:  
                print("Too much other expense ")
                c=input("want to reduce other expense (yes/no)")
                if c=="yes":
                    print("use free parking space instaed of paid ")
                    print("if using cash for toll payment than reduce it by fastage ") 
                elif c=="no":
                    print("increse your budget by")
                    print(total_trip_cost-budget+(total_trip_cost-budget))
                else:
                    print("enter valid input")     
else:
    print(" ***enough budget*** ")


