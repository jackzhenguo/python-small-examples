import os
from collections import defaultdict
d = defaultdict(list)
for root, dirs, files in os.walk('E:\guozhen3\08LOL\JDLOL\fengbi\jdlol'):
    for file in files:
        abs_path_file = os.path.join(root, file)
        file_size = os.path.getsize(abs_path_file)
        d[abs_path_file].append(file_size)
