from datetime import time
time1 = time(12, 30, 45)
print(time1)
time2 = time(9, 15, 0)
print(time2)
duration = time1.hour - time2.hour
print("Duration in hours:", duration)
difference = time1.minute - time2.minute
print("Difference in minutes:", difference)
change = time1.second - time2.second
print("Change in seconds:", change)
need_to_add = time(0, 45, 30)
new_time = time1.hour + need_to_add.hour, time1.minute + need_to_add.minute, time1.second + need_to_add.second
print("New time after adding duration:", new_time)