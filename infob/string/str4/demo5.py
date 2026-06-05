n=input(" enter the string --")
i=0
count=0
alpha=""
while i<len(n):
    ch=n[i]
    if ch not in alpha:
        alpha=alpha+ch
        count=count+1
    i=i+1
print("count is--", count)
print("alphabets are --", alpha)
