import datetime
dob="15-08-2000"
dob=datetime.datetime.strptime(dob, "%d-%m-%Y")
today=datetime.datetime.now()
age=today.year-dob.year-((today.month, today.day)<(dob.month, dob.day))
print("Age is:",age)
time_remaining=dob.replace(year=today.year)-today
if time_remaining.days<0:
    time_remaining=dob.replace(year=today.year+1)-today
print("Time remaining for next birthday:",time_remaining.days,"days")
time_remaining_hours=time_remaining.seconds//3600
time_remaining_minutes=(time_remaining.seconds//60)%60
time_remaining_seconds=time_remaining.seconds%60
print("Time remaining for next birthday:",time_remaining_hours,"hours",time_remaining_minutes,"minutes",time_remaining_seconds,"seconds")
