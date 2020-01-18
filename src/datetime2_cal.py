from datetime import date, datetime
from time import localtime, strftime, strptime


today_date = date.today()
print(today_date)  # 2019-12-22

today_time = datetime.today()
print(today_time)  # 2019-12-22 18:02:33.398894

local_time = localtime()
print(strftime("%Y-%m-%d %H:%M:%S", local_time))  # 转化为定制的格式

# parse str time to struct time
struct_time = strptime('2019-12-22 10:10:08', "%Y-%m-%d %H:%M:%S")
print(strftime("%m-%d-%Y %H:%M:%S", struct_time))  # 转化为定制的格式
