def batchCreate(ps='.md',start=100,n=100,path='.'):
    import os
    import calendar
    for i in range(start,start+n):
        with open(path+'/'+str(i)+ps,'w') as fw:
            
            fw.write("""
                       ```markdown
			@author jackzhenguo
			@desc 
			@date 2020/1/1
			```
		     """.format()
    print('done')
