
'''5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website'''

n=input("enter website").lower()
if n[0]=="w" and n[1]=='w' and n[2]=='w' and n[-1]=='m' and n[-2]=='o' and n[-3]=='c' and n[-4]=='.':
    print(n,"is valid website ")
else:
    print("invalide website ")
