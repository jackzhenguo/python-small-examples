import pandas as pd
import os


file_folder = '此处输入待处理的文件夹位置'
files = os.listdir(file_folder)
for file in files:
    file_loc = file_folder + '/' + file
    raw_data = pd.read_csv(file_loc,header = None)
    data_after_process = raw_data.iloc[:,0].str.split(';',expand = True)
    data_after_process_loc = '处理完毕后的数据存储位置'+ '/' + file
    data_after_process.to_csv(data_after_process_loc,index=None, header= None)
