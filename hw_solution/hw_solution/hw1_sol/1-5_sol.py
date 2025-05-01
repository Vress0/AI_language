import time

curr_total_sec = time.time()
curr_total_sec = int(curr_total_sec)
curr_total_min, curr_sec = divmod(curr_total_sec,60)
curr_total_hour, curr_min = divmod(curr_total_min,60)
curr_total_day, curr_hour = divmod(curr_total_hour,24)
print(str(curr_hour).zfill(2)+':'+str(curr_min).zfill(2)+':'+str(curr_sec).zfill(2))
