import os
import datetime

print(datetime.datetime.now())
print(f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_modify_time(dir):
    for root,dirs,files in os.walk(dir): #dir下的所有文件和子文件件夹
        for file in files:
            absPathFile=os.path.join(root,file)
            print(type(os.path.getmtime(absPathFile)))
            modefiedTime=datetime.datetime.fromtimestamp(os.path.getmtime(absPathFile))
            now=datetime.datetime.now()
            diffTime=now-modefiedTime
            if diffTime.days < 20:#条件筛选:最近20天内的文件
                print(f"{absPathFile:<27s}  修改时间[{modefiedTime.strftime('%Y-%m-%d %H:%M:%S')}] 距今[{diffTime.days:3d}天{diffTime.seconds//3600:2d}时 {diffTime.seconds%3600//60:2d}分]")#打印相关信息
                
get_modify_time('.')

