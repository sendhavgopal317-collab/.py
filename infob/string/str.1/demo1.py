n=input("enter feetback  -").lower()
i=0
count=0   
while i<len(n):
       ch=n[i]
       if ch in "aeiou":
        count=count+1
       i=i+1
print(count) 