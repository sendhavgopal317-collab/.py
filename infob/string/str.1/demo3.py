n=input("enter product review ")
oc=input("enter the characte to check")
count=0
for i in n:
    if oc in i:
        count=count+1
print("count of", oc,"in","review",count)