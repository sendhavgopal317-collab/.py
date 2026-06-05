n=int(input("enter size "))
countA=0
countB=0
countC=0
countF=0
arr=[]
arrA=[]
arrB=[]
arrC=[]
arrfail=[]
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    if arr[i]>=90:
        arrA.append(arr[i])
        countA=countA+1
    elif arr[i]>=75:
        arrB.append(arr[i])
        countB+=1
    elif arr[i]>=50:
        arrC.append(arr[i])
        countC+=1
    else:
        arrfail.append(arr[i])
        countF+=1
print("A grade student ", arrA ,"number of students ",countA)
print("B grade student ", arrB ,"number of students ",countB)
print("C grade student ", arrC ,"number of students ",countC)
print("Fail grade student ", arrfail ,"number of students ",countF)



