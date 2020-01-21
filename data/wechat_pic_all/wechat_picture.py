# import requests
# from lxml import etree
# import pandas as pd
# import re

# url = 'https://www.zhihu.com/question/335825565'
# with requests.get(url) as res:
#     content = res.content
#     print(content)
#     html = etree.HTML(content)
#     imgs = html.xpath('//figure//img/@src')
#     print(imgs)



# method2: 直接手动复制到本地，然后提取图片地址
import os
import re
from urllib.request import urlopen

with open('./data/wechat_pic.html',mode='r',errors='ignore') as f: 
    lines = f.readlines()
    pic_urls = re.findall(r'<img src="(.*?).jpg"',lines[0])
    pic_urls = [pic for pic in pic_urls if pic.startswith('https')] # 只保留以https开头的地址
    #pic_urls = set(pic_urls) # 直接使用set会打破原来顺序，因为原网页按照图片分类，所以直接使用set去重，效果不佳
    downloaded = []
    for i,url in enumerate(pic_urls):
        if url in downloaded:
            continue
        print(f'{url}')
        q=urlopen(url+'.jpg')
        pic=q.read()
        
        save = open('./data/wechat_pic/%d.jpg'%(i,),mode='w+b')
        save.write(pic)
        q.close()
        save.close()
        print(f'pic{i} saved!')
        downloaded.append(url)
      


# import cv2
# import  numpy as np
 
# #均值哈希算法
# def aHash(img):
#     #缩放为8*8
#     img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
#     #转换为灰度图
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     #s为像素和初值为0，hash_str为hash值初值为''
#     s=0
#     hash_str=''
#     #遍历累加求像素和
#     for i in range(8):
#         for j in range(8):
#             s=s+gray[i,j]
#     #求平均灰度
#     avg=s/64
#     #灰度大于平均值为1相反为0生成图片的hash值
#     for i in range(8):
#         for j in range(8):
#             if  gray[i,j]>avg:
#                 hash_str=hash_str+'1'
#             else:
#                 hash_str=hash_str+'0'
#     return hash_str

# img1=cv2.imread('A.png')
# img2=cv2.imread('B.png')
# hash1= aHash(img1)
# hash2= aHash(img2)
# print(hash1)
# print(hash2)
# n=cmpHash(hash1,hash2)
# print '均值哈希算法相似度：'+ str(n)

