u = int(input("Enter the Number of Unit:"))

if u <= 100:
	print("Charge:",5*u)
elif u <=200:
       print("charge:" , (u-100)*7 + 100*5)
elif u > 200 :
	print("charge:",(u-200)*10 + (100)*7 + (100*5))