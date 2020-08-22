def batchCreate(ps='.md',n=100,path='.'):
    import os
    for i in range(n):
        with open(path+'/'+str(i)+ps,'w') as fw:
            fw.write('')
    print('done')
