from collections import namedtuple
books=namedtuple("std",["book_id", "title","authore","price"])
n=int(input("enter the number of books"))
book=[]
for i in range(n):
    print("enter details ")
    name=input("enter id ")
    t=(input("enter title "))
    auth=(input("enter authore "))
    p=input("enter price")
    s=books(name,t,auth,p)
    book.append(s)
for x in book:
    print(x.book_id,"and",x.title,"and ", x.authore,x.price)


high=0
low=float('inf')
sum=0
for i in book:
    if (i.price)>high:
        sum+=i.price
        high=i.price
        emph=(i.book_id,i.title,i.authore,i.price)
    if i.price<low:
        low=i.price
        emph=(i.book_id,i.title,i.authore,i.price)

print("highest salary",emph)
print("lowest salary",empl)
av=sum/n
print("average is ",av)
for i in book:
   if (i.price)>int(av):
    print(i.book_id,i.title,i.authore,i.price)
   


   
