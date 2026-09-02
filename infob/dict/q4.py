students={"aman":78,"ajay":92,"ravi":00,"neha":85}
l=0
s=float("inf")
for x in students:
    if students[x]<s:
        s=students[x]
        sts=x
    if students[x]>l:
        l=students[x]
        stl=x
print(stl,"get highest",l)
print(sts," gets lowest",s)

