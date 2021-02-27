# function: give each *.md example to a navigation in bottom of file
# author: zhenguo
# date: 2021.2.27
# version: 1.0

import os

for file in os.listdir('../md'):
    if os.path.splitext(file)[-1] == '.md':
        with open('../md/' + file, 'a') as f:
            file_name = os.path.splitext(file)[0]
            try:
                c = '\n\n<center>[上一个例子](%s.md)    [下一个例子](%s.md)</center>' % (str(int(file_name) - 1), str(int(file_name) + 1))
                f.write(c)
                print('文件%s写入成功' % (file,))
            except:
                print(ex)
