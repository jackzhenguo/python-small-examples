======
5.2 xlsx文件合并
======

.. code:: python

    #将文件夹中xlsx文件合并到一个excel文件中
    import xlrd
    import os
    import pandas as pd
    import glob 
    from numpy import *
    import  pandas as pd
    location = 'C:/Users/CQ375/Desktop/ex'
    fileList = []
    n=0
    for fileName in os.walk(location):
        for table in fileName[2]:
            path = fileName[0] + '/' + table 
            Li=pd.read_excel(path,header=0)
            n = n+1 
            fileList.append(Li)
            print('第' + str(n) + '个表格已合并')
    print("在该目录下有%d个xlsx文件"%len(fileList))
    data_result = pd.concat(fileList,ignore_index=True)
    data_result.to_excel('C:/Users/CQ375/Desktop/ex/test.xlsx',index=0)

