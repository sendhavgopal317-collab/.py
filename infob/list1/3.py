'''comprehension list in python '''
a=[1,2,3,4,5,6]
#b=[i*3 for i in a]
#print(b)
#b=[val for val in a if val%2==0]
#print(b)
#b=[val*val for val in a if val>3 and val%2==0]
#print(b)
b=["even " if x%2==0 else "odd" for x in a]
print(b)
c=[x*10  if x%2==0 else x*20 for x in a]
print(c)
