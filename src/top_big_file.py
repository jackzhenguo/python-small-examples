import os
from collections import namedtuple


def top_big_file(mydir, n=10):
    lst = []
    FileProp = namedtuple('FileProp', ['file_path', 'file_size'])
    for root, dirs, files in os.walk(mydir):
        for file in files:
            abs_path = os.path.join(root, file)
            si = os.stat(abs_path).st_size / 1024 / 1024  # MB
            fp = FileProp(abs_path, round(si, 3))
            lst.append(fp)

    lst = sorted(lst, key=lambda x: x.file_size, reverse=True)
    top10 = [x for i, x in enumerate(lst) if i < n]
    print(top10)


top_big_file('.')

# [FileProp(file_path='.\\md2\\Python之路.pdf', file_size=3.118), FileProp(file_path='.\\.git\\objects\\7d\\5416afddb0bfe6de1089824f2dfb39b1ea4fcc', file_size=3.063), FileProp(file_path='.\\.git\\objects\\da\\f4589ab2e1647a9b3ce5c3e3ba48d909baec19', file_size=3.051), FileProp(file_path='.\\exts\\main.dic', file_size=2.917), FileProp(file_path='.\\.git\\objects\\43\\bffe17d4c89e259ff069fa3b7c2129e5fb04eb', file_size=2.884), FileProp(file_path='.\\.git\\objects\\73\\07314b8666bb088e9864d95b989fd9b748008f', file_size=1.206), FileProp(file_path='.\\.git\\objects\\e4\\83d8240ef9c97acd11daec1d37adddee17321e', file_size=1.088), FileProp(file_path='.\\.git\\objects\\ee\\ebe0dafc66a1e914ddb7bd55bdfceaf4b56798', file_size=1.088), FileProp(file_path='.\\.git\\objects\\89\\a98b536bf4be1b6c7c8a37885458cc0c6e5111', file_size=0.339), FileProp(file_path='.\\img\\turtlesnow2.gif', file_size=0.329)]