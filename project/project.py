import random
print("=============================")
print("   TREASURE HUNT ADVENTURE   ")
print("=============================")
print("Rules")
print("1. Start with 3 lives.")
print("2. start with 5 rounds")
print("3. Find treasure to increase score.")
print("4. Avoid enemies.")
print("5. Game ends when lives become 0 or round become 0.")
#player variable
lives=3
score=0
coins=0
round=1
while lives>0:
 print("-"*20)
 print("Treasure hunting ")
 print("-"*20)
 difficulty=(input("Enter to start :-"))
 if difficulty not in("1") :
   print("enter valid type")
   continue
 else :
  match difficulty:
   case "1":
    print("1 :- To go straight")
    print("2 :- To turn left")
    print("3 :- To turn right ")   
    d=int(input("enter direction :-- "))
    if d>3:
     print("Enter valid direction")
     continue
    if d==1:
     event=random.randint(1,8)
     if event==1: 
      print("1 :- To go straight")
      print("2 :- To turn left")
      print("3 :- To turn right ")
      n=int(input("enter next direction :-- "))
      if n>3:
       print("Enter valid direction")
       
       if n==1: 
        print("You won 10 coin ")
        coins=coins+10
        print("----------------")
        print("Lives :", lives)
        print("Score :", score)
        print("Coins :", coins)
        print("----------------")
        continue
       elif n==2:
         print("wild wolf infront fo you")
         print("1 :- fight")
         print("2:-  hide")
         print("3 :- run")
         a=int(input("enter action :-"))
         if a==2:
           print("wolf passed you can come out")
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           d2=int(input("enter next direction :-- "))
           if d2>3:
             print("enter valid direction")
             continue
           else:
             if d2==1:
               print("treasure found")
               score=score+50
               print("----------------")
               print("score ", score)
               print("lives :-", lives)
               print("----------------")

             elif d2==2:
               print("cought by enemy")
               lives=lives-1
               score=score+50
               print("----------------")
               print("score :-",score)
               print("lives :-", lives)
               print("----------------")
               if lives==0:
                 break
             else:
               print("Eagle dropped coins")
               coins=coins+100
               score=score+100
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
         elif a==1:
           result=random.randint(1)
           if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction :--"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no):--")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")

               else:
                 s=random.randint(1,2)
                 print("1:- To turn left")
                 print("2 :- To turn right ")
                 dir=int(input("enter next step :-- "))
                 if dir<3:
                   print("Dark cave full of bats")
                   print("1:- enter")
                   print("2:- leave")
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                   else:
                       print("succesfully leaved cave")
                       print("attacked")  
                       print("you were dead")
                       lives=lives-1
                       print("----------------")
                       print("coins=",coins)
                       print("score=",score)
                       print("coins=",coins)
                       print("----------------")
                 else:
                   print("enter a valid direction")
                   continue
           elif a==2:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
               if lives==0:
                 break
       elif n==3:
         print("sword found")
         print("dragon seen ")
         print("1:-attack :: 2:-defend :: 3:- run")    
         b=int(input("enter action :--"))
         if b==1:
           print("you win")
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           d2=int(input("enter next direction:-- "))
           if d2>3:
             print("Enter valid direction")
             continue
           else:
             if d2==1:
               print("!!Treasure found!!")
               score=score+50
               print("score ", score)
               print("lives :-", lives)
             elif d2==2:
               print("cought by enemy")
               lives=lives-1
               score=score+50
               print("----------------")
               print("score :-",score)
               print("lives :-", lives)
               print("----------------")
               if lives==0:
                 break
             elif d2==3:
                print("Eagle dropped coins")
                coins=coins+100
                continue
         elif b==2:
             print(" you are safe  ")
             print("Go ahead")
             print("Treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             r=int(input("enter direction :--"))
             if r<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no):--")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 s=random.randint(1,2)
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 direction=int(input("enter next step :--"))
                 if direction<=3:
                   if direction==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")

                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")

                   elif direction==2:
                     print("Dark cave full of bats")
                     print("1:- enter")
                     print("2:- leave")
                     enter=int(input("enter or leave :--"))
                     if enter==1:
                       print("treasure found")
                       lives=live+1
                       score=score+200
                       coins=coins+500
                       print("----------------")
                       print("coins=",coins)
                       print("score=",score)
                       print("coins=",coins)
                       print("----------------")
                     else:
                       print("attacked")  
                       print("you were dead")
                       lives=lives-1
                       print("----------------")
                       print("coins=",coins)
                       print("score=",score)
                       print("coins=",coins)
                       print("----------------")
                   elif direction==3:
                      print("stranger seen")
                      z=int(input("1:- Talk :: 2:-ignore ::-- "))
                      if z==1:
                        print("you were killed")
                        lives=lives-1
                        print("----------------")
                        print("lives:",lives)
                        print("coins:",coins)
                        print("----------------")
                      else:
                        print("Taken you to treasure ")
                        print("!!You won!!")
                        coins=coins+1000
                        score=score+1000
                        print("----------------")
                        print("coins:-",coins)
                        print("lives:-",lives)
                        print("score:-",score)
                        print("----------------")
                     
                 else:
                   print("enter a valid direction")
                   continue
             elif r==2:
               print("cought by enemy")
               lives=lives-1
               score=score+50
               print("----------------")
               print("score :-",score)
               print("lives :-", lives)
               print("----------------")
               if lives==0:
                 break
             elif d2==3:
                print("Eagle dropped coins")
                coins=coins+100
         elif b==3:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
               print("1 :- To go straight")
               print("2 :- To turn left")
               print("3 :- To turn right ")
               p=int(input("enter next direction :--"))
               if p==1:
                print("You found old Treasure map")
                print("1:- follow map :: 2:-ignore map")
                i=int(input("enter your choice:--"))
                o=random.randint(1,2)
                if i>2:
                 print("enter valid choice")
                elif i==1:
                 print("found a treasure")
                 print("!!congratulation!!")
                 lives=lives+1
                 score=score+500
                 coins=coins+200
                 score=score+1000
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
               else:
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 q=int(input("enter next direction:--"))
                 w=random.randint(1,3)
                 if w==1:
                    print("entered in village")
                    print("1:-talk to know about treasure::2:-leave")
                    u=int(input("enter :-- "))
                    if u==1:
                      print("villager give you hint treasure in CAVE")
                      print("treasuround ")
                      print("!!congratulation!!")      
                      lives=lives+1
                      score=score+500
                      coins=coins+200
                      print("----------------")
                      print("score =", score)
                      print("coins =", coins)
                      print("lives+1=", lives)
                      print("----------------")
                    if u==2 :
                     print("wolf want to join you")
                     print("1: accept , 2:- reject")
                     q=int(input("enter you choice:--"))
                     v=random.randint(1,2)
                     if v>2:
                       print("enter valid choice")
                     elif v==1:
                       print("you were killed by wolf")
                       lives=lives-1
                       print("----------------")
                       print("score =", score)
                       print("coins =", coins)
                       print("lives=", lives)
                       print("----------------")
                     elif v==2:
                      print("Treasure found succesfully")
                      print("you are safe")
                      lives=lives+1
                      score=score+500
                      coins=coins+200
                      print("----------------")
                      print("score =", score)
                      print("coins =", coins)
                      print("lives=", lives)
                      print("----------------")
                 elif w==2:
                      print("found a secret password")
                      print("continue walking....")
                      print("found locked door")
                      password=(input("enter password :--"))
                      if password=="dragon123".lower():
                        print("Door opened ")
                        print("Treasure found")
                        lives=lives+1
                        score=score+500
                        coins=coins+200
                        print("----------------")
                        print("score =", score)
                        print("coins =", coins)
                        print("lives+1=", lives)
                        print("----------------")
                      else:
                       print("wrong password")
                       print("killed by dragon")
                       lives=lives-1
                       print("----------------")
                       print("score =", score)
                       print("coins =", coins)
                       print("lives+1=",lives)
                       print("----------------")
                       if lives==0:
                        break
                 elif w==3:
                    print("You found time portal")
                    print("1:-undo lost lives")
                    print("get help to found treasure")
                    e=int(input("enter choice:--"))
                    if e==1:
                      lives=lives+3
                      print("lives =", lives)
                    else:
                     print("treasure found")
                     print("Treasure hunter")
                     lives=lives+1
                     score=score+500
                     coins=coins+200
                     print("----------------")
                     print("score =", score)
                     print("coins =", coins)
                     print("lives=",lives)
                     print("----------------")
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
               if lives==0:
                 break     
         else:
           if b>3:
             print("enter valid direction")
         
     elif event==2 :
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- to turn right ") 
       p=int(input("enter next direction:-- "))
       if p>3:
         print("enter a valid direction")
         continue
       else:
        if p==1:
         print("coin bag found")
         coins=coins+500
         print("----------------")
         print("Lives :", lives)
         print("Score :", score)
         print("Coins :", coins)
         print("----------------")
         continue
        if p==2:
         print("stranger seen")
         z=int(input("1:- Talk :: 2:-ignore :-- "))
         if z==1:
          g=random.randint(1,2)
          if g==1:
            print("you were killed")
            lives=lives-1
            print("----------------")
            print("lives:",lives)
            print("coins:",coins)
            print("----------------")
          else:
            print("Taken you to treasure ")
            print("!!You won!!")
            coins=coins+1000
            print("----------------")
            print("coins:-",coins)
            print("lives:-",lives)
            print("----------------")
        else:
         print("found nothing")
         print("Better luck next time")
         print("----------------")
         print("coins:-",coins)
         print("lives:-",lives)
         print("----------------")
     elif event==3: 
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction :--"))
       if p>3:
         print("enter a valid direction")
         continue
       else:
         if p<=2:
           print("you found a treasure")
           score=score+500
           print("----------------")
           print("score=",score)
           print("lives=",lives)
           print("----------------")
         else:
           print("you got 150 coins")
           coins=coins+150
           print("enemy killed you")
           lives=lives-1
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
           if lives==0:
             break
     elif event==4:
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction:--"))
       if p==1:
         print("You found old Treasure map")
         print("1:- follow map :: 2:-ignore map")
         i=int(input("enter your choice :--"))
         o=random.randint(1,2)
         if i>2:
           print("enter valid choice")
         elif i==1:
           print("found a treasure")
           print("!!congratulation!!")
           lives=lives+1
           score=score+500
           coins=coins+200
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
         else:
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           q=int(input("enter next direction"))
           w=random.randint(1,3)
           if w==1:
             print("entered in village")
             print("1:-talk to know about treasure::2:-leave")
             u=int(input("enter :--"))
             if u==1:
               print("villager give you hint treasure in CAVE")
               print("treasur found ")
               print("!!congratulation!!")      
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             if u==2 :
               print("wolf want to join you")
               print("1: accept , 2:- reject")
               t=int(input("enter you choice :--"))
               v=random.randint(1,2)
               if v>2:
                 print("enter valid choice")
               elif v==1:
                 print("you were killed by wolf")
                 lives=lives-1
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
               elif v==2:
                 print("Treasure found succesfully")
                 print("you are safe")
                 lives=lives+1
                 score=score+500
                 coins=coins+200
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
           elif w==2:
             print("found a secret password")
             print("continue walking....")
             print("found locked door")
             password=(input("enter password :--")).lower()
             if password=="dragon123".lower():
               print("Door opened ")
               print("Treasure found")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             else:
               print("wrong password")
               print("killed by dragon")
               lives=lives-1
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
               if lives==0:
                 break
           elif w==3:
             print("You found time portal")
             print("1:-undo lost lives")
             print("get help to found treasure")
             e=int(input("enter choice:--"))
             if e==1:
               lives=lives+3
               print("lives =", lives)
             else:
               print("treasure found")
               print("Treasure hunter")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
       elif p==2:
          print("sword found")
          print("dragon seen ")
          print("1:-attack :: 2:-hide :: 3:- run")    
          a=int(input("enter action :-"))
          if a==2:
           print("wolf passed you can come out")
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           d2=int(input("enter next direction"))
           if d2>3:
             print("enter valid direction")
             continue
           else:
             if d2==1:
               print("treasure found")
               score=score+50
               print("----------------")
               print("score ", score)
               print("lives :-", lives)
               print("----------------")
             elif d2==2:
               print("cought by enemy")
               live=lives-1
               score=score+50
               print("----------------")
               print("score :-",score)
               print("lives :-", lives)
               print("----------------")
               if lives==0:
                 break
             elif d2==3:
                print("Eagle dropped coins")
                coins=coins+100
                continue
          elif a==1:
           result=random.randint(1,2)
           if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no)")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 dir=int(input("enter next step"))
                 if dir<=3:
                   print("Dark cave full of bats")
                   print("1:- enter")
                   print("2:- leave")
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                 else:
                   print("enter a valid direction")
                   continue
          elif a==3:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
               print("found nothing")
               lives=lives-1
               print("--"*25)
               print("lives:--",lives)
               print("score:--",score)
               print("coin:--",coins)
               print("-"*25)
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
               if lives==0:
                 break  
       elif p==3:           
           result=random.randint(1,2)
           if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no)")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 s=random.randint(1,2)
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 dir=int(input("enter next step"))
                 if dir<=3:
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                   elif dir==2:
                     print("Dark cave full of bats")
                     print("1:- enter")
                     print("2:- leave")
                     enter=int(input("enter or leave"))
                     if enter==1:
                       print("treasure found")
                       lives=live+1
                       score=score+200
                       coins=coins+500
                       print("----------------")
                       print("coins=",coins)
                       print("score=",score)
                       print("coins=",coins)
                       print("----------------")
                     else:
                       print("attacked")  
                       print("you were dead")
                       lives=lives-1
                       print("----------------")
                       print("coins=",coins)
                       print("score=",score)
                       print("coins=",coins)
                       print("----------------")
                   elif dir==3:
                      print("stranger seen")
                      z=int(input("1:- Talk :: 2:-ignore :: "))
                      if z==1:
                       g=random.randint(1,2)
                       if g<1:
                        print("you were killed")
                        lives=lives-1
                        print("----------------")
                        print("lives:",lives)
                        print("coins:",coins)
                        print("----------------")
                      else:
                        print("Taken you to treasure ")
                        print("!!You won!!")
                        coins=coins+1000
                        score=score+1000
                        print("----------------")
                        print("coins:-",coins)
                        print("lives:-",lives)
                        print("score:-",score)
                        print("----------------")
                      
     elif event==5:
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction"))
       if p>3:
         print("enter valid direction")
         continue
       else:
         if p==1:
           print("WELL DONE ! Treasure found")
           lives=lives+1
           score=score+50
         else:
           if p==2 or p==3 :
             print("Enemy appeared")
             lives=lives-1
             round=round-1
             score=score+100
             print("----------------")
             print("score =", score)
             print("coins =", coins)
             print("lives+1=", lives)
             print("----------------")
             if lives==0:
               break 
     elif event>=6:
        if event==8:
         print("You are trapped")
         print("End game")
         lives=lives-1
         print("----------------")
         print("score =", score)
         print("coins =", coins)
         print("lives+1=", lives)
         print("----------------")
         if lives==0:
           break 
        else:
         print("You found a Treasure")
         print("you are treasure hunter")
         score=score+50 
         print("----------------")
         print("score =", score)
         print("coins =", coins)
         print("live=", lives)  
         print("----------------")  
         continue
     decide=input("do you want to continue(yes/no)").lower()      
     if decide=="yes":
      if lives<1 or round>4:
         print("===== GAME OVER =====")
         print("Final Score :", score)
         print("Coins :", coins)
         print("Lives :", lives)
         break
      else:
        round=round-1
        continue
     else:
      print("===== GAME OVER =====")
      print("Final Score :", score)
      print("Coins :", coins)
      print("Lives :", lives)
      break
    elif d==2:
     event=random.randint(1,8)
     if event==1: 
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       n=int(input("enter next direction"))
       if n==1: 
        print("You won 10 coin ")
        coins=coins+10
        print("----------------")
        print("lives=",lives)
        print("score=",score+500)
        print("----------------")
        continue
       elif n==2:
         print("wild wolf infront fo you")
         print("1 :- fight")
         print("2:-  hide")
         print("3 :- run")
         a=int(input("enter action :-"))
         if a==2:
           print("wolf passed you can come out")
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           d2=int(input("enter next direction"))
           if d2>3:
             print("enter valid direction")
             continue
           else:
             if d2==1:
               print("treasure found")
               score=score+50
               print("score ", score)
               print("lives :-", lives)
             elif d2==2:
               print("cought by enemy")
               live=lives-1
               score=score+50
               print("----------------")
               print("score :-",score)
               print("lives :-", lives)
               print("----------------")
               if lives==0:
                 break
             elif d2==3:
                print("Eagle dropped coins")
                coins=coins+100
                continue
         elif a==1:
           result=random.randint(1,2)
           if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no)")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 s=random.randint(1,2)
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 dir=int(input("enter next step"))
                 if dir<=3:
                   print("Dark cave full of bats")
                   print("1:- enter")
                   print("2:- leave")
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                 else:
                   print("enter a valid direction")
                   continue
         elif a==3:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
               if lives==0:
                 break
       elif n==3:
          print("sword found")
          print("dragon seen ")
          print("1:-attack :: 2:-defend :: 3:- run")    
          a=int(input("enter action :-"))
          if a==1:
            result=random.randint(1,2)
            if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no)")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 s=random.randint(1,2)
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 dir=int(input("enter next step"))
                 if dir<=3:
                   print("Dark cave full of bats")
                   print("1:- enter")
                   print("2:- leave")
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                 else:
                   print("enter a valid direction")
                   continue
            
          elif a==2:
           result=random.randint(1,2)
           if result==1:
             print(" you win ")
             print("treasure key found ")
             print("1 :- To go straight")
             print("2 :- To turn left")
             print("3 :- To turn right ")   
             a=int(input("enter direction"))
             if a<=3:
               print("Treasure door found ")
               print("enter or not(yes/no)")
               dis=input("enter your dicission(yes/no)")
               if dis=="yes":
                 s=random.randint(1,2)
                 if s==1:
                   print("Treasure found")
                   print("!! congratulation!! you won")
                   score=score+500
                   lives=lives+1
                   print("----------------")
                   print("lives= ", lives)
                   print("score= ", score)
                   print("----------------")
                 if s==2:
                   print("It's a trap ")
                   print("you are trapped")
                   lives=lives-1
                   print("----------------")
                   print("score= ", score)
                   print("lives= ", lives) 
                   print("----------------")
               else:
                 s=random.randint(1,2)
                 print("1 :- To go straight")
                 print("2 :- To turn left")
                 print("3 :- To turn right ")
                 dir=int(input("enter next step"))
                 if dir<=3:
                   print("Dark cave full of bats")
                   print("1:- enter")
                   print("2:- leave")
                   if dir==1:
                     print("successfully found treasure")
                     print("!! congratulation !!")
                     score=score+500
                     lives=lives+1
                     print("----------------")
                     print("score=",score)
                     print("lives=",lives)
                     print("----------------")
                 else:
                   print("enter a valid direction")
                   continue
          elif a==3:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
               if live==0:
                 break      
         
     elif event==2 :
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ") 
       p=int(input("enter next direction"))
       if p==1:
         print("coin bag found")
         coins=coins+500
         print("----------------")
         print("score=",score)
         print("lives=",lives)
         print("score=",score+500)
         print("----------------")
         continue
       if p==2:
         print("stranger seen")
         z=int(input("1:- Talk :: 2:-ignore :: "))
         if z==1:
          g=random.randint(1,2)
          if g==1:
            print("you were killed")
            lives=lives-1
            print("----------------")
            print("lives:",lives)
            print("coins:",coins)
            print("----------------")
         else:
            print("Taken you to treasure ")
            print("!!You won!!")
            print("----------------")
            coins=coins+1000
            print("coins:-",coins)
            print("lives:-",lives)
            print("----------------")
       else:
         print("found nothing")
         print("Better luck next time")
         print("----------------")
         print("coins:-",coins)
         print("lives:-",lives)
         print("----------------")
     elif event==3: 
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction"))
       if p>3:
         print("enter a valid direction")
         continue
       else:
         if p<=2:
           print("you found a treasure")
           score=score+500
           print("----------------")
           print("score=",score)
           print("lives=",lives)
           print("----------------")
           continue
         else:
           print("you got 150 coins")
           coins=coins+150
           print("enemy killed you")
           lives=lives-1
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
           if lives==0:
             break
     elif event==4:
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction"))
       if p==1:
         print("You found old Treasure map")
         print("1:- follow map :: 2:-ignore map")
         i=int(input("enter your choice"))
         o=random.randint(1,2)
         if i>2:
           print("enter valid choice")
         elif i==1:
           print("found a treasure")
           print("!!congratulation!!")
           lives=lives+1
           score=score+500
           coins=coins+200
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
         else:
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           q=int(input("enter next direction"))
           w=random.randint(1,3)
           if w==1:
             print("entered in village")
             print("1:-talk to know about treasure::2:-leave")
             u=int(input("enter ::-"))
             if u==1:
               print("villager give you hint treasure in CAVE")
               print("treasure found ")
               print("!!congratulation!!")      
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             if u==2 :
               print("wolf want to join you")
               print("1: accept , 2:- reject")
               t=int(input("enter you choice"))
               v=random.randint(1,2)
               if v>2:
                 print("enter valid choice")
               elif v==1:
                 print("you were killed by wolf")
                 lives=lives-1
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
               elif v==2:
                 print("Treasure found succesfully")
                 print("you are safe")
                 lives=lives+1
                 score=score+500
                 coins=coins+200
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
           elif w==2:
             print("found a secret password")
             print("continue walking....")
             print("found locked door")
             password=(input("enter password")).lower()
             if password=="dragon123".lower():
               print("Door opened ")
               print("Treasure found")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             else:
               print("wrong password")
               print("killed by dragon")
               lives=lives-1
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
               if lives==0:
                 break
           elif w==3:
             print("You found time portal")
             print("1:-undo lost lives")
             print("get help to found treasure")
             e=int(input("enter choice:"))
             if e==1:
               lives=lives+3
               print("lives =", lives)
             else:
               print("treasure found")
               print("Treasure hunter")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
       elif p==2:
          print("WELL DONE ! Treasure found")
          lives=lives+1
          score=score+500
          print("----------------")
          print("score =", score)
          print("coins =", coins)
          print("lives+1=", lives) 
          print("----------------")
       else:
         print("found nothing")
         print("Better luck next time")
         print("----------------")
         print("coins:-",coins)
         print("lives:-",lives)
         print("----------------")
             
     elif event==5:
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction"))
       if p>3:
         print("enter valid direction")
         continue
       else:
         if p==1:
           print("WELL DONE ! Treasure found")
           lives=lives+1
           score=score+500
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
         else:
           if p==2:
             print("Enemy appeared")
             lives=lives-1
             round=round-1
             print("----------------")
             print("score =", score)
             print("coins =", coins)
             print("lives+1=", lives)
             print("----------------")
             if lives==0:
               break 
     elif event>=6:
        if event==8:
         print("You are trapped")
         print("End game")
         lives=lives-1
         print("----------------")
         print("score =", score)
         print("coins =", coins)
         print("lives+1=", lives)
         print("----------------")
         if lives==0:
           break 
        else:
         print("You found a Treasure")
         print("you are treasure hunter")
         score=score+50 
         print("----------------")
         print("score =", score)
         print("coins =", coins)
         print("live=", lives)   
         print("----------------")
         continue
     decide=input("do you want to continue(yes/no)").lower()      
     if decide=="yes":
      if lives<1 or round>4:
         print("===== GAME OVER =====")
         print("Final Score :", score)
         print("Coins :", coins)
         print("Lives :", lives)
         break
      else:
        round=round-1
        continue
     else:
      print("===== GAME OVER =====")
      print("Final Score :", score)
      print("Coins :", coins)
      print("Lives :", lives)
      break    
    elif d==3:
     event=random.randint(1,3)
     if event==1: 
        print("bomb infront of you")
        print("1:-cut red wire")
        print("2:-cut blue wire")
        print("3:-Run")
        c=int(input("enter choice :-"))
        if c==1:
         s=random.randint(1,2)
         if s==1:
           print("bomb blast")
           print("you were died")
           lives=lives-1 
           print("----------------")
           print("lives= ",lives)
           print("score=", score)
           print("----------------")
         else:
           if s==2:
             print("diffused successfully")
             print("got lives+score+coins")
             coins=coins+400
             lives=lives+1
             score=score+500
             print("----------------")
             print("lives= ",lives)
             print("score=", score)
             print("coins ", coins+100)
             print("----------------")
           else:
             print("print a valid command")  
        elif c==2:
         d=random.randint(1,2)
         print("cutting wire")
         if d==1:
           print("bomb blast")
           print("you were died")
           lives=lives-1 
           print("----------------")
           print("lives= ",lives)
           print("score=", score)
           print("----------------")
         else:
           if d==2:
             print("diffused successfully")
             print("got lives+score+coins")
             coins=coins+400
             lives=lives+1
             score=score+500
             print("----------------")
             print("lives= ",lives)
             print("score=", score)
             print("----------------")
           else:
             print("print a valid command")
        else:
             j=random.randint(1,2)
             if j==1:
               print("escaped succesfully")
             else:
               print("caught died")
               lives=lives-1
               print("----------------")
               print("score=",score)
               print("lives=",lives)
               print("----------------")
     elif event==2:
       print("1 :- To go straight")
       print("2 :- To turn left")
       print("3 :- To turn right ")
       p=int(input("enter next direction"))
       if p==1:
         print("You found old Treasure map")
         print("1:- follow map :: 2:-ignore map")
         i=int(input("enter your choice"))
         o=random.randint(1,2)
         if i>2:
           print("enter valid choice")
         elif i==1:
           print("found a treasure")
           print("!!congratulation!!")
           lives=lives+1
           score=score+500
           coins=coins+200
           print("----------------")
           print("score =", score)
           print("coins =", coins)
           print("lives+1=", lives)
           print("----------------")
         else:
           print("1 :- To go straight")
           print("2 :- To turn left")
           print("3 :- To turn right ")
           q=int(input("enter next direction"))
           w=random.randint(1,3)
           if w==1:
             print("entered in village")
             print("1:-talk to know about treasure::2:-leave")
             u=int(input("enter ::-"))
             if u==1:
               print("villager give you hint treasure in CAVE")
               print("treasuround ")
               print("!!congratulation!!")      
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             if u==2 :
               print("wolf want to join you")
               print("1: accept , 2:- reject")
               t=int(input("enter you choice"))
               v=random.randint(1,2)
               if v>2:
                 print("enter valid choice")
               elif v==1:
                 print("you were killed by wolf")
                 lives=lives-1
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
               elif v==2:
                 print("Treasure found succesfully")
                 print("you are safe")
                 lives=lives+1
                 score=score+500
                 coins=coins+200
                 print("----------------")
                 print("score =", score)
                 print("coins =", coins)
                 print("lives+1=", lives)
                 print("----------------")
           elif w==2:
             print("found a secret password")
             print("continue walking....")
             print("found locked door")
             password=int(input("enter password")).lower()
             if password=="dragon123".lower():
               print("Door opened ")
               print("Treasure found")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             else:
               print("wrong password")
               print("killed by dragon")
               lives=lives-1
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
               if lives==0:
                 break
           elif w==3:
             print("You found time portal")
             print("1:-undo lost lives")
             print("get help to found treasure")
             e=int(input("enter choice:"))
             if e==1:
               lives=lives+3
               print("lives =", lives)
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
             else:
               print("treasure found")
               print("Treasure hunter")
               lives=lives+1
               score=score+500
               coins=coins+200
               print("----------------")
               print("score =", score)
               print("coins =", coins)
               print("lives+1=", lives)
               print("----------------")
     else:
        print("\nYou are inside the Snow Cave.")

        print("1. Search")
        print("2. Dig the snow")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
         print("You found a golden key! 🔑")
         score += 10

        elif choice == 2:
         print("You dug into the snow and found the treasure! 💰")
         score += 20

        else:
          print("You left the cave without finding anything.") 
    decide=input("do you want to continue(yes/no)").lower()      
    if decide=="yes":
      if lives<1 or round>4:
         print("===== GAME OVER =====")
         print("Final Score :", score)
         print("Coins :", coins)
         print("Lives :", lives)
         break
      else:
        round=round-1
        continue
    else:
      print("===== GAME OVER =====")
      print("Final Score :", score)
      print("Coins :", coins)
      print("Lives :", lives)
      break
           


      # ==============================
# REVERSE TREASURE HUNT GAME
# Python 3.10+
# ==============================

   case 2:
     print("=" * 50)
     print("      REVERSE TREASURE HUNT")
     print("=" * 50)

     clues = []
     answers = []

     print("\nTEAM 1 : CREATE THE TREASURE HUNT")
     print("--------------------------------")

     n = int(input("How many clues do you want? "))

     for i in range(n):
      print("\nClue", i + 1)

      clue = input("Enter clue : ")
      ans = input("Enter answer : ")

      clues.append(clue.lower())
      answers.append(ans.lower())

     print("\n" * 30)
     print("Team 2 Turn")
     print("=" * 50)

     score = 0
     current = 0

     while current < n:
 
      print("\nLevel", current + 1)
      print("Clue :", clues[current])

      guess = input("Answer : ").lower()

      if guess == answers[current]:
        print("Correct!")
        score += 10
        current += 1
      else:
        print("Wrong Answer")

        print("\nChoose Option")
        print("1. Try Again")
        print("2. Skip (-5 points)")
        print("3. Quit")

        choice = int(input("Enter choice : "))

        match choice:

            case 1:
                continue

            case 2:
                print("Skipped")
                score -= 5
                current += 1

            case 3:
                print("Game Over")
                break

            case _:
                print("Invalid Choice")

     print("\n")
     print("=" * 50)
     print("GAME FINISHED")
     print("=" * 50)

     print("Final Score :", score)

     match score:

      case s if s >= n * 10:
        print("Excellent! Treasure Found!")

      case s if s >= (n * 5):
        print("Good Job!")

      case s if s > 0:
        print("You Found Some Clues!")

      case _:
        print("Better Luck Next Time!")

     print("=" * 50)
 
