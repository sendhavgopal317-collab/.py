'''nstant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop'''
n=input("enter message ")
i=0
s=0
rev=""
final=""
while i<len(n):
    ch=n[i]
    if ch==" " or i==len(n)-1:
               
          j=i
          for j in range(j,s-1,-1):
              ch=n[j]
              rev=rev+ch
          s=i
       
    i=i+1
print(rev)
