'''2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP
'''
n=input("enter the string")
s=(n.split())
i=len(s)
while i>=0:
 print((s[i])[-1:0:-1],end=" ")
 i=i-1