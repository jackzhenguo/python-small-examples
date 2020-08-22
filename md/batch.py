def batchCreate(ps='.md',start=100,n=100,path='.'):
    import os
    for i in range(start,start+n):
        with open(path+'/'+str(i)+ps,'w') as fw:
            fw.write('')
    print('done')
