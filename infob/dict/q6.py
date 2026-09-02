students={"aman":78,"ajay":39,"ravi":65,"neha":85}
passing=50
for x in students:
    if students[x]>passing:
        print(x ," is passed",students[x])
    else:
        print(x ," is failed",students[x])

