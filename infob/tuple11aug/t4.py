
n1=int(input("enter size of 1st "))
n2=int(input("enter size of 2nd "))
n3=int(input("enter size of 3rd "))
arr1=[]
arr2=[]
arr3=[]
for i in range(n1):
    arr1.append(int(input("enter elements 1 ")))
for i in range(n2):
    arr2.append(int(input("enter elements 2")))
for i in range(n3):
    arr3.append(int(input("enter elements 3 ")))
common=[]
for i in range (n1):
      num=arr1[i]
      if num not in common:
       for j in range(n2):
           if num==arr2[j]:
            if num not in common: 
                for k in range(n3):
                     if num==arr3[k]:
                          common.append(num)
                          break
print(common)

    

    

    