n=int(input("enter number of house"))
total=0
sum=0
largest=0
for i in range(n):
    u=int(input("enter unit  comsumed"))
    if u>200:
        bill=((u-200)*10+100*7+100*5)
    elif u>100:
        bill=((u-100)*7+100*5)
    else:
        bill=(u*5)
    if bill>2000:
        bill=bill+bill(bill*10)/100
    elif u<50:
        bill=bill-100    
    if bill>largest:
        largest=bill
    sum=sum+bill
    print("bill of",i+1 ,"=",bill)
print("total=",sum)
print("largest=",largest)