"""
@author jackzhenguo
@desc 批量生成模板文件
@tag datetime file
@version v1.2
@date 2020/8/23
"""

import os
import calendar
from datetime import date,datetime

def getEverydaySince(year,month,day,n=10):
    i = 0
    _, days = calendar.monthrange(year, month)
    while i < n: 
        d = date(year,month,day)    
        if day == days:
            month,day = month+1,0
            _, days = calendar.monthrange(year, month)
            if month == 13:
                year,month = year+1,1
                _, days = calendar.monthrange(year, month)
        yield d
        day += 1
        i += 1


def batchCreate(ps='.md',start=100,n=100,path='.',year=2020,month=2,day=1):
  
    for i,day in zip(range(start,start+n),\
                     getEverydaySince(year,month,day,n) \
                    ):
        with open(path+'/'+str(i)+ps,'w') as fw:
            
            fw.write("""
```markdown
@author jackzhenguo
@desc
@tag
@version 
@date {}
```
		     """.format(datetime.strftime(day,'%Y/%m/%d'))\
		     )
            print(day)
    print('done')
