'''utility toolkit system'''
import math
while True:
        print("1:- check prime number")
        print("2:- check polindrome number")
        print("3:- reverse a number")
        print("4:- count digit")
        print("5:- exit")
        choose=int(input("enter your choice :- "))
        match choose :
            case 1:
                    n=int(input("enter number :-"))
                    if n<2:
                           print("not prime ")
                    else:
                           i=2
                           while i<=int(math.sqrt(n)):
                                  if n%i==0:
                                         print("not prime")
                                         break
                                  i=i+1
                           else:
                                  print("prime")
            case 3:
                      n=int(input("enter number :- "))  
                      rev=0
                      while n>0:
                             digit=n%10
                             rev=rev*10+digit
                             n=n//10  
                      print(rev)                        
            case 2:
                      n=int(input("enter number :-"))
                      rev=0
                      temp=n
                      while n>0:
                             digit=n%10
                             rev=rev*10+digit
                             n=n//10
                      #if rev==n:
                      #       print("polindrom")
                      #else:
                       #      print("not polindrom")           
                      print(rev)
                      if rev==temp:
                             print("polindrom")
                      else:
                             print("not polindrom")
                             print(rev)
            case 4 :   
                   n=int(input("enter number :-")) 
                   count=0
                   while n>0:
                      digit=n%10 
                      count=count+1
                      n=n//10
                   print("count:- ", count)
            case 5:
                      print("exit")
                      break
        again=input("do you want to continue (yes/no)").lower()                              
        match again: 
               case "yes":
                      continue
               case "no":
                      print("exit")
                      break
               case __:
                      print("invalid input")
                      break
print("THANKS")
               
          