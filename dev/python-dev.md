### Python 实战


#### 221 自动群发邮件

Python自动群发邮件

```python
import smtplib
from email import (header)
from email.mime import (text, application, multipart)
import time

def sender_mail():
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    sender, password = '113097485@qq.com', "**************"
    smt_p.login(sender, password)
    receiver_addresses, count_num = [
        'guozhennianhua@163.com', 'xiaoxiazi99@163.com'], 1
    for email_address in receiver_addresses:
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = "zhenguo"
            msg['To'] = email_address
            msg['subject'] = header.Header('这是邮件主题通知', 'utf-8')
            msg.attach(text.MIMEText(
                '这是一封测试邮件，请勿回复本邮件~', 'plain', 'utf-8'))
            smt_p.sendmail(sender, email_address, msg.as_string())
            time.sleep(10)
            print('第%d次发送给%s' % (count_num, email_address))
            count_num = count_num + 1
        except Exception as e:
            print('第%d次给%s发送邮件异常' % (count_num, email_address))
            continue
    smt_p.quit()

sender_mail()
```



注意：
发送邮箱是qq邮箱，所以要在qq邮箱中设置开启SMTP服务，设置完成时会生成一个授权码，将这个授权码赋值给文中的`password`变量

#### 222 二分搜索

二分搜索是程序员必备的算法，无论什么场合，都要非常熟练地写出来。

小例子描述：
在**有序数组**`arr`中，指定区间`[left,right]`范围内，查找元素`x`
如果不存在，返回`-1`

二分搜索`binarySearch`实现的主逻辑

```python
def binarySearch(arr, left, right, x):
    while left <= right:

        mid = int(left + (right - left) / 2); # 找到中间位置。求中点写成(left+right)/2更容易溢出，所以不建议这样写

        # 检查x是否出现在位置mid
        if arr[mid] == x:
            print('found %d 在索引位置%d 处' %(x,mid))
            return mid

            # 假如x更大，则不可能出现在左半部分
        elif arr[mid] < x:
            left = mid + 1 #搜索区间变为[mid+1,right]
            print('区间缩小为[%d,%d]' %(mid+1,right))

        # 同理，假如x更小，则不可能出现在右半部分
        elif x<arr[mid]:
            right = mid - 1 #搜索区间变为[left,mid-1]
            print('区间缩小为[%d,%d]' %(left,mid-1))

    # 假如搜索到这里，表明x未出现在[left,right]中
    return -1
```

在`Ipython`交互界面中，调用`binarySearch`的小Demo:

```python
In [8]: binarySearch([4,5,6,7,10,20,100],0,6,5)
区间缩小为[0,2]
found 5 at 1
Out[8]: 1

In [9]: binarySearch([4,5,6,7,10,20,100],0,6,4)
区间缩小为[0,2]
区间缩小为[0,0]
found 4 at 0
Out[9]: 0

In [10]: binarySearch([4,5,6,7,10,20,100],0,6,20)
区间缩小为[4,6]
found 20 at 5
Out[10]: 5

In [11]: binarySearch([4,5,6,7,10,20,100],0,6,100)
区间缩小为[4,6]
区间缩小为[6,6]
found 100 at 6
Out[11]: 6
```

#### 223 爬取天气数据并解析温度值

爬取天气数据并解析温度值

素材来自朋友袁绍，感谢！

爬取的html 结构

<img src="./img/1.png" width="50%"/>

```python
import requests
from lxml import etree
import pandas as pd
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml#input'
with requests.get(url) as res:
    content = res.content
    html = etree.HTML(content)
```



通过lxml模块提取值

lxml比beautifulsoup解析在某些场合更高效

```python
location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
```

结果：

```python
['香河', '涿州', '唐山', '沧州', '天津', '廊坊', '太原', '石家庄', '涿鹿', '张家口', '保定', '三河', '北京孔庙', '北京国子监', '中国地质博物馆', '月坛公
园', '明城墙遗址公园', '北京市规划展览馆', '什刹海', '南锣鼓巷', '天坛公园', '北海公园', '景山公园', '北京海洋馆']

['11/-5°C', '14/-5°C', '12/-6°C', '12/-5°C', '11/-1°C', '11/-5°C', '8/-7°C', '13/-2°C', '8/-6°C', '5/-9°C', '14/-6°C', '11/-4°C', '13/-3°C'
, '13/-3°C', '12/-3°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-2°C', '12/-2°C', '12/-3°C']
```


构造DataFrame对象

```python
df = pd.DataFrame({'location':location, 'temperature':temperature})
print('温度列')
print(df['temperature'])
```

正则解析温度值

```python
df['high'] = df['temperature'].apply(lambda x: int(re.match('(-?[0-9]*?)/-?[0-9]*?°C', x).group(1) ) )
df['low'] = df['temperature'].apply(lambda x: int(re.match('-?[0-9]*?/(-?[0-9]*?)°C', x).group(1) ) )
print(df)
```

详细说明子字符创捕获

除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用`()`表示的就是要提取的分组（group）。比如：`^(\d{3})-(\d{3,8})$`分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码

```python
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 010-12345
# 010
# 12345
```

如果正则表达式中定义了组，就可以在`Match`对象上用`group()`方法提取出子串来。

注意到`group(0)`永远是原始字符串，`group(1)`、`group(2)`……表示第1、2、……个子串。


最终结果

```kepython
Name: temperature, dtype: object
    location temperature  high  low
0         香河     11/-5°C    11   -5
1         涿州     14/-5°C    14   -5
2         唐山     12/-6°C    12   -6
3         沧州     12/-5°C    12   -5
4         天津     11/-1°C    11   -1
5         廊坊     11/-5°C    11   -5
6         太原      8/-7°C     8   -7
7        石家庄     13/-2°C    13   -2
8         涿鹿      8/-6°C     8   -6
9        张家口      5/-9°C     5   -9
10        保定     14/-6°C    14   -6
11        三河     11/-4°C    11   -4
12      北京孔庙     13/-3°C    13   -3
13     北京国子监     13/-3°C    13   -3
14   中国地质博物馆     12/-3°C    12   -3
15      月坛公园     12/-3°C    12   -3
16   明城墙遗址公园     13/-3°C    13   -3
17  北京市规划展览馆     12/-2°C    12   -2
18       什刹海     12/-3°C    12   -3
19      南锣鼓巷     13/-3°C    13   -3
20      天坛公园     12/-2°C    12   -2
21      北海公园     12/-2°C    12   -2
22      景山公园     12/-2°C    12   -2
23     北京海洋馆     12/-3°C    12   -3
```

### 十、数据分析

本项目基于Kaggle电影影评数据集，通过这个系列，你将学到如何进行数据探索性分析(EDA)，学会使用数据分析利器`pandas`，会用绘图包`pyecharts`，以及EDA时可能遇到的各种实际问题及一些处理技巧。



本项目需要导入的包：

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Bar,Grid,Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType
```

#### 1 创建DataFrame
pandas中一个dataFrame实例：
```python
Out[89]:
        a  val
0  apple1  1.0
1  apple2  2.0
2  apple3  3.0
3  apple4  4.0
4  apple5  5.0
```

我们的**目标**是变为如下结构：
```python
a  apple1  apple2  apple3  apple4  apple5
0     1.0     2.0     3.0     4.0     5.0
```

乍看可使用`pivot`，但很难一步到位。

所以另辟蹊径，提供一种简单且好理解的方法：

```python
In [113]: pd.DataFrame(index=[0],columns=df.a,data=dict(zip(df.a,df.val)))
Out[113]:
a  apple1  apple2  apple3  apple4  apple5
0     1.0     2.0     3.0     4.0     5.0
```
以上方法是重新创建一个DataFrame,直接把`df.a`所有可能取值作为新dataframe的列，index调整为`[0]`，注意类型必须是数组类型(array-like 或者 Index)，两个轴确定后，`data`填充数据域。

```python
In [116]: dict(zip(df.a,df.val))
Out[116]: {'apple1': 1.0, 'apple2': 2.0, 'apple3': 3.0, 'apple4': 4.0, 'apple5': 5.0}
```



#### 2 导入数据
数据来自kaggle，共包括三个文件：

1. movies.dat
2. ratings.dat
3. users.dat

`movies.dat`包括三个字段：['Movie ID', 'Movie Title', 'Genre']

使用pandas导入此文件：

```python
import pandas as pd

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::', engine='python', header=None, names = ['Movie ID', 'Movie Title', 'Genre'])
```

导入后，显示前5行：

```python
   Movie ID                                        Movie Title  \
0         8      Edison Kinetoscopic Record of a Sneeze (1894)   
1        10                La sortie des usines Lumi猫re (1895)   
2        12                      The Arrival of a Train (1896)   
3        25  The Oxford and Cambridge University Boat Race ...   
4        91                         Le manoir du diable (1896)   
5       131                           Une nuit terrible (1896)   
6       417                      Le voyage dans la lune (1902)   
7       439                     The Great Train Robbery (1903)   
8       443        Hiawatha, the Messiah of the Ojibway (1903)   
9       628                    The Adventures of Dollie (1908)  
                                          Genre  
0                             Documentary|Short  
1                             Documentary|Short  
2                             Documentary|Short  
3                                           NaN  
4                                  Short|Horror  
5                           Short|Comedy|Horror  
6  Short|Action|Adventure|Comedy|Fantasy|Sci-Fi  
7                    Short|Action|Crime|Western  
8                                           NaN  
9                                  Action|Short  
```



次导入其他两个数据文件

`users.dat`:

```python
users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Twitter ID'])
print(users.head())
```

结果：

```python
   User ID  Twitter ID
0        1   397291295
1        2    40501255
2        3   417333257
3        4   138805259
4        5  2452094989
5        6   391774225
6        7    47317010
7        8    84541461
8        9  2445803544
9       10   995885060
```



`rating.data`:

```python
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])
print(ratings.head())
```

结果：

```python
   User ID  Movie ID  Rating  Rating Timestamp
0        1    111161      10        1373234211
1        1    117060       7        1373415231
2        1    120755       6        1373424360
3        1    317919       6        1373495763
4        1    454876      10        1373621125
5        1    790724       8        1374641320
6        1    882977       8        1372898763
7        1   1229238       9        1373506523
8        1   1288558       5        1373154354
9        1   1300854       8        1377165712
```

 **read_csv 使用说明**

说明，本次导入`dat`文件使用`pandas.read_csv`函数。

第一个位置参数`./data/movietweetings/ratings.dat` 表示文件的相对路径

第二个关键字参数：`delimiter='::'`，表示文件分隔符使用`::`

后面几个关键字参数分别代表使用的引擎，文件没有表头，所以`header`为`None;`

导入后dataframe的列名使用`names`关键字设置，这个参数大家可以记住，比较有用。



Kaggle电影数据集第一节，我们使用数据处理利器 `pandas`， 函数`read_csv` 导入给定的三个数据文件。

```python
import pandas as pd

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::', engine='python', header=None, names = ['Movie ID', 'Movie Title', 'Genre'])
users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Twitter ID'])
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])
```

用到的`read_csv`，某些重要的参数，如何使用在上一节也有所提到。下面开始数据探索分析(EDA)

> 找出得分前10喜剧(comedy)



#### 3 处理组合值

表`movies`字段`Genre`表示电影的类型，可能有多个值，分隔符为`|`，取值也可能为`None`.

针对这类字段取值，可使用Pandas中Series提供的`str`做一步转化，**注意它是向量级的**，下一步，如Python原生的`str`类似，使用`contains`判断是否含有`comedy`字符串：

```python
mask = movies.Genre.str.contains('comedy',case=False,na=False)
```

注意使用的两个参数：`case`, `na`

case为 False，表示对大小写不敏感；
na Genre列某个单元格为`NaN`时，我们使用的充填值，此处填充为`False`

返回的`mask`是一维的`Series`，结构与 movies.Genre相同，取值为True 或 False.

观察结果：

```python
0    False
1    False
2    False
3    False
4    False
5     True
6     True
7    False
8    False
9    False
Name: Genre, dtype: bool

```


 #### 4 访问某列

得到掩码mask后，pandas非常方便地能提取出目标记录：

```python
comedy = movies[mask]
comdey_ids = comedy['Movie ID']

```

以上，在pandas中被最频率使用，不再解释。看结果`comedy_ids.head()`：

```python
5      131
6      417
15    2354
18    3863
19    4099
20    4100
21    4101
22    4210
23    4395
25    4518
Name: Movie ID, dtype: int64

```



1-4介绍`数据读入`，`处理组合值`，`索引数据`等, pandas中使用较多的函数，基于Kaggle真实电影影评数据集，最后得到所有`喜剧 ID`：

```python
5      131
6      417
15    2354
18    3863
19    4099
20    4100
21    4101
22    4210
23    4395
25    4518
Name: Movie ID, dtype: int64

```

下面继续数据探索之旅~

#### 5 连接两个表

拿到所有喜剧的ID后，要想找出其中平均得分最高的前10喜剧，需要关联另一张表：`ratings`:

再回顾下ratings表结构：

```python
   User ID  Movie ID  Rating  Rating Timestamp
0        1    111161      10        1373234211
1        1    117060       7        1373415231
2        1    120755       6        1373424360
3        1    317919       6        1373495763
4        1    454876      10        1373621125
5        1    790724       8        1374641320
6        1    882977       8        1372898763
7        1   1229238       9        1373506523
8        1   1288558       5        1373154354
9        1   1300854       8        1377165712

```


pandas 中使用`join`关联两张表，连接字段是`Movie ID`，如果顺其自然这么使用`join`：

```python
combine = ratings.join(comedy, on='Movie ID', rsuffix='2')

```

左右滑动，查看完整代码

大家可验证这种写法，仔细一看，会发现结果非常诡异。

究其原因，这是pandas join函数使用的一个算是坑点，它在官档中介绍，连接右表时，此处右表是`comedy`，它的`index`要求是连接字段，也就是 `Movie ID`. 

左表的index不要求，但是要在参数 `on`中给定。

**以上是要注意的一点**

修改为：

```python
combine = ratings.join(comedy.set_index('Movie ID'), on='Movie ID')
print(combine.head(10))

```

以上是OK的写法

观察结果：

```python
   User ID  Movie ID  Rating  Rating Timestamp Movie Title Genre
0        1    111161      10        1373234211         NaN   NaN
1        1    117060       7        1373415231         NaN   NaN
2        1    120755       6        1373424360         NaN   NaN
3        1    317919       6        1373495763         NaN   NaN
4        1    454876      10        1373621125         NaN   NaN
5        1    790724       8        1374641320         NaN   NaN
6        1    882977       8        1372898763         NaN   NaN
7        1   1229238       9        1373506523         NaN   NaN
8        1   1288558       5        1373154354         NaN   NaN
9        1   1300854       8        1377165712         NaN   NaN

```

Genre列为`NaN`表明，这不是喜剧。需要筛选出此列不为`NaN` 的记录。

#### 6 按列筛选

pandas最方便的地方，就是向量化运算，尽可能减少了for循环的嵌套。

按列筛选这种常见需求，自然可以轻松应对。

为了照顾初次接触 pandas 的朋友，分两步去写：

```python
mask = pd.notnull(combine['Genre'])

```

结果是一列只含`True 或 False`的值

```python
result = combine[mask]
print(result.head())

```

结果中，Genre字段中至少含有一个Comedy字符串，表明验证了我们以上操作是OK的。

```python
    User ID  Movie ID  Rating  Rating Timestamp             Movie Title  \
12        1   1588173       9        1372821281      Warm Bodies (2013)   
13        1   1711425       3        1372604878        21 & Over (2013)   
14        1   2024432       8        1372703553   Identity Thief (2013)   
17        1   2101441       1        1372633473  Spring Breakers (2012)   
28        2   1431045       7        1457733508         Deadpool (2016)   

                             Genre  
12           Comedy|Horror|Romance  
13                          Comedy  
14    Adventure|Comedy|Crime|Drama  
17              Comedy|Crime|Drama  
28  Action|Adventure|Comedy|Sci-Fi  


```



截止目前已经求出所有喜剧电影`result`，前5行如下，Genre中都含有`Comedy`字符串：
```python
    User ID  Movie ID  Rating  Rating Timestamp             Movie Title  \
12        1   1588173       9        1372821281      Warm Bodies (2013)   
13        1   1711425       3        1372604878        21 & Over (2013)   
14        1   2024432       8        1372703553   Identity Thief (2013)   
17        1   2101441       1        1372633473  Spring Breakers (2012)   
28        2   1431045       7        1457733508         Deadpool (2016)   

                             Genre  
12           Comedy|Horror|Romance  
13                          Comedy  
14    Adventure|Comedy|Crime|Drama  
17              Comedy|Crime|Drama  
28  Action|Adventure|Comedy|Sci-Fi  
```



#### 7 按照Movie ID 分组

result中会有很多观众对同一部电影的打分，所以要求得分前10的喜剧，先按照`Movie ID`分组，然后求出平均值：
```python
score_as_movie = result.groupby('Movie ID').mean()
```

前5行显示如下：
```python
               User ID  Rating  Rating Timestamp
Movie ID                                        
131       34861.000000     7.0      1.540639e+09
417       34121.409091     8.5      1.458680e+09
2354       6264.000000     8.0      1.456343e+09
3863      43803.000000    10.0      1.430439e+09
4099      25084.500000     7.0      1.450323e+09
```

#### 8 按照电影得分排序

```python
score_as_movie.sort_values(by='Rating', ascending = False,inplace=True)
score_as_movie
```
前5行显示如下：
```python
	User ID	Rating	Rating Timestamp
Movie ID			
7134690	30110.0	10.0	1.524974e+09
416889	1319.0	10.0	1.543320e+09
57840	23589.0	10.0	1.396802e+09
5693562	50266.0	10.0	1.511024e+09
5074	43803.0	10.0	1.428352e+09
```
都是满分？这有点奇怪，会不会这些电影都只有几个人评分，甚至只有1个？评分样本个数太少，显然最终的平均分数不具有太强的说服力。

所以，下面要进行每部电影的评分人数统计

#### 9 分组后使用聚合函数

根据`Movie ID`分组后，使用`count`函数统计`每组个数`，只保留count列，最后得到`watchs2`:

```python
watchs = result.groupby('Movie ID').agg(['count'])
watchs2 = watchs['Rating']['count']
```
打印前20行：
```python
print(watchs2.head(20))
```
结果：
```python
Movie ID
131      1
417     22
2354     1
3863     1
4099     2
4100     1
4101     1
4210     1
4395     1
4518     1
4546     2
4936     2
5074     1
5571     1
6177     1
6414     3
6684     1
6689     1
7145     1
7162     2
Name: count, dtype: int64
```
果然，竟然有这么多电影的评论数只有1次！样本个数太少，评论的平均值也就没有什么说服力。

查看`watchs2`一些重要统计量：
```python
watchs2.describe()
```
结果：
```python
count    10740.000000
mean        20.192086
std         86.251411
min          1.000000
25%          1.000000
50%          2.000000
75%          7.000000
max       1843.000000
Name: count, dtype: float64
```
共有10740部**喜剧**电影被评分，平均打分次数20次，标准差86，75%的电影样本打分次数小于7次，最小1次，最多1843次。

#### 10 频率分布直方图

绘制评论数的频率分布直方图，便于更直观的观察电影被评论的分布情况。上面分析到，75%的电影打分次数小于7次，所以绘制打分次数小于20次的直方图：

```python
fig = plt.figure(figsize=(12,8))
histn = plt.hist(watchs2[watchs2 <=19],19,histtype='step')
plt.scatter([i+1 for i in range(len(histn[0]))],histn[0])
```

![](./img/20200131094927.jpg)

`histn`元祖表示个数和对应的被分割的区间，查看`histn[0]`:
```python
array([4383., 1507.,  787.,  541.,  356.,  279.,  209.,  163.,  158.,
        118.,  114.,   90.,  104.,   81.,   80.,   73.,   62.,   65.,
         52.])
```
```python
sum(histn[0]) # 9222
```
看到电影评论次数1到19次的喜剧电影9222部，共有10740部喜剧电影，大约`86%`的喜剧电影评论次数`小于20次`，有`1518`部电影评论数不小于20次。

我们肯定希望挑选出被评论次数尽可能多的电影，因为难免会有水军和滥竽充数等`异常评论`行为。那么，如何准确的量化最小抽样量呢？



#### 11 最小抽样量

根据统计学的知识，最小抽样量和Z值、样本方差和样本误差相关，下面给出具体的求解最小样本量的计算方法。

采用如下计算公式：

$$ n = \frac{Z^2\sigma^2}{E^2} $$


此处，$Z$ 值取为95%的置信度对应的Z值也就是1.96，样本误差取为均值的2.5%.

根据以上公式，编写下面代码：

```python
n3 = result.groupby('Movie ID').agg(['count','mean','std'])
n3r = n3[n3['Rating']['count']>=20]['Rating']
```
只计算影评超过20次，且满足最小样本量的电影。计算得到的`n3r`前5行：
```python
	count	mean	std
Movie ID			
417	22	8.500000	1.263027
12349	68	8.485294	1.227698
15324	20	8.350000	1.039990
15864	51	8.431373	1.374844
17925	44	8.636364	1.259216
```
进一步求出最小样本量：
```python
nmin = (1.96**2*n3r['std']**2) / ( (n3r['mean']*0.025)**2 )
```
`nmin`前5行：
```python
Movie ID
417         135.712480
12349       128.671290
15324        95.349276
15864       163.434005
17925       130.668350
```

筛选出满足最小抽样量的喜剧电影：

```python
n3s = n3r[ n3r['count'] >= nmin ]
```
结果显示如下，因此共有`173`部电影满足最小样本抽样量。

```python

count	mean	std
Movie ID			
53604	129	8.635659	1.230714
57012	207	8.449275	1.537899
70735	224	8.839286	1.190799
75686	209	8.095694	1.358885
88763	296	8.945946	1.026984
...	...	...	...
6320628	860	7.966279	1.469924
6412452	276	7.510870	1.389529
6662050	22	10.000000	0.000000
6966692	907	8.673649	1.286455
7131622	1102	7.851180	1.751500
173 rows × 3 columns
```

#### 12 去重和连表

按照平均得分从大到小排序：
```python
n3s_sort = n3s.sort_values(by='mean',ascending=False)
```
结果：
```python
	count	mean	std
Movie ID			
6662050	22	10.000000	0.000000
4921860	48	10.000000	0.000000
5262972	28	10.000000	0.000000
5512872	353	9.985836	0.266123
3863552	199	9.010050	1.163372
...	...	...	...
1291150	647	6.327666	1.785968
2557490	546	6.307692	1.858434
1478839	120	6.200000	0.728761
2177771	485	6.150515	1.523922
1951261	1091	6.083410	1.736127
173 rows × 3 columns
```
仅靠`Movie ID`还是不知道哪些电影，连接`movies`表：
```python
ms = movies.drop_duplicates(subset=['Movie ID'])
ms = ms.set_index('Movie ID')
n3s_final = n3s_drops.join(ms,on='Movie ID')
```

#### 13 结果分析

喜剧榜单前50名：
```python
Movie Title
Five Minutes (2017)
MSG 2 the Messenger (2015)
Avengers: Age of Ultron Parody (2015)
Be Somebody (2016)
Bajrangi Bhaijaan (2015)
Back to the Future (1985)
La vita 鐚?bella (1997)
The Intouchables (2011)
The Sting (1973)
Coco (2017)
Toy Story 3 (2010)
3 Idiots (2009)
Green Book (2018)
Dead Poets Society (1989)
The Apartment (1960)
P.K. (2014)
The Truman Show (1998)
Am鑼卨ie (2001)
Inside Out (2015)
Toy Story 4 (2019)
Toy Story (1995)
Finding Nemo (2003)
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)
Home Alone (1990)
Zootopia (2016)
Up (2009)
Monsters, Inc. (2001)
La La Land (2016)
Relatos salvajes (2014)
En man som heter Ove (2015)
Snatch (2000)
Lock, Stock and Two Smoking Barrels (1998)
How to Train Your Dragon 2 (2014)
As Good as It Gets (1997)
Guardians of the Galaxy (2014)
The Grand Budapest Hotel (2014)
Fantastic Mr. Fox (2009)
Silver Linings Playbook (2012)
Sing Street (2016)
Deadpool (2016)
Annie Hall (1977)
Pride (2014)
In Bruges (2008)
Big Hero 6 (2014)
Groundhog Day (1993)
The Breakfast Club (1985)
Little Miss Sunshine (2006)
Deadpool 2 (2018)
The Terminal (2004)
```

前10名评论数图：

![](./img/2020013109495711.jpg)

代码：
```python
x = n3s_final['Movie Title'][:10].tolist()[::-1]
y = n3s_final['count'][:10].tolist()[::-1]
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('评论数',y,category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="喜剧电影被评论次数"),
                    toolbox_opts=opts.ToolboxOpts(),)
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)
grid.render_notebook()
```

前10名得分图：

![](./img/2020013109500812.jpg)

代码：
```python
x = n3s_final['Movie Title'][:10].tolist()[::-1]
y = n3s_final['mean'][:10].round(3).tolist()[::-1]
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('平均得分',y,category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="喜剧电影平均得分"),
                    xaxis_opts=opts.AxisOpts(min_=8.0,name='平均得分'),
                    toolbox_opts=opts.ToolboxOpts(),)
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)
grid.render_notebook()
```



#### 14 生成哑变量

分类变量的数值化，是指将枚举类变量转化为indicator变量或称dummy变量。

那么什么是`indicator变量`，看看如下例子，A变量解析为：`[1,0,0]`, B解析为：`[0,1,0]`, C解析为：`[0,0,1]`
```python
In [8]: s = pd.Series(list('ABCA'))
In [9]: pd.get_dummies(s)
Out[9]:
   A  B  C
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
```

如果输入的字符有4个唯一值，看到字符a被解析为[1,0,0,0]，向量长度为4.

```python
In [5]: s = pd.Series(list('abaccd'))
In [6]: pd.get_dummies(s)
Out[6]:
   a  b  c  d
0  1  0  0  0
1  0  1  0  0
2  1  0  0  0
3  0  0  1  0
4  0  0  1  0
5  0  0  0  1
```

也就是说dummy向量的长度等于输入字符串中，唯一字符的个数。

#### 15 讨厌的SettingWithCopyWarning！！！

Pandas 处理数据，太好用了，谁用谁知道！

使用过 Pandas 的，几乎都会遇到一个警告：

*SettingWithCopyWarning*

非常烦人！

尤其是刚接触 Pandas 的，完全不理解为什么弹出这么一串：

```python
d:\source\test\settingwithcopy.py:9: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy 
```

归根结底，是因为代码中出现`链式操作`...

有人就问了，什么是`链式操作`?

这样的：

```python
tmp = df[df.a<4]
tmp['c'] = 200
```

先记住这个最典型的情况，即可！

有的人就问了：出现这个 Warning, 需要理会它吗？ 

如果结果不对，当然要理会；如果结果对，不care.

举个例子~~

```python
import pandas as  pd

df = pd.DataFrame({'a':[1,3,5],'b':[4,2,7]},index=['a','b','c'])
df.loc[df.a<4,'c'] = 100
print(df)
print('it\'s ok')

tmp = df[df.a<4]
tmp['c'] = 200
print('-----tmp------')
print(tmp)
print('-----df-------')
print(df)
```

输出结果：
```python
   a  b      c
a  1  4  100.0
b  3  2  100.0
c  5  7    NaN
it's ok
d:\source\test\settingwithcopy.py:9: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy     
  tmp['c'] = 200
-----tmp------
   a  b    c
a  1  4  200
b  3  2  200
-----df-------
   a  b      c
a  1  4  100.0
b  3  2  100.0
c  5  7    NaN
```

it's ok 行后面的发生链式赋值，导致结果错误。因为 tmp 变了，df 没赋上值啊，所以必须理会。

it's ok 行前的是正解。

以上，链式操作尽量避免，如何避免？多使用 `.loc[row_indexer,col_indexer]`，提示告诉我们的~

#### 16 NumPy 数据归一化、分布可视化

仅使用 `NumPy`，下载数据，归一化，使用 `seaborn` 展示数据分布。

**下载数据**

```python
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
wid = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[1])
```
仅提取 `iris` 数据集的第二列 `usecols = [1]`

**展示数据**

```python
array([3.5, 3. , 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3. ,
       3. , 4. , 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6, 3.3, 3.4, 3. ,
       3.4, 3.5, 3.4, 3.2, 3.1, 3.4, 4.1, 4.2, 3.1, 3.2, 3.5, 3.1, 3. ,
       3.4, 3.5, 2.3, 3.2, 3.5, 3.8, 3. , 3.8, 3.2, 3.7, 3.3, 3.2, 3.2,
       3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 2. , 3. , 2.2, 2.9, 2.9,
       3.1, 3. , 2.7, 2.2, 2.5, 3.2, 2.8, 2.5, 2.8, 2.9, 3. , 2.8, 3. ,
       2.9, 2.6, 2.4, 2.4, 2.7, 2.7, 3. , 3.4, 3.1, 2.3, 3. , 2.5, 2.6,
       3. , 2.6, 2.3, 2.7, 3. , 2.9, 2.9, 2.5, 2.8, 3.3, 2.7, 3. , 2.9,
       3. , 3. , 2.5, 2.9, 2.5, 3.6, 3.2, 2.7, 3. , 2.5, 2.8, 3.2, 3. ,
       3.8, 2.6, 2.2, 3.2, 2.8, 2.8, 2.7, 3.3, 3.2, 2.8, 3. , 2.8, 3. ,
       2.8, 3.8, 2.8, 2.8, 2.6, 3. , 3.4, 3.1, 3. , 3.1, 3.1, 3.1, 2.7,
       3.2, 3.3, 3. , 2.5, 3. , 3.4, 3. ])
      
```

这是单变量(univariate)长度为 150 的一维 NumPy 数组。

**归一化**

求出最大值、最小值
```python
smax = np.max(wid)
smin = np.min(wid)

In [51]: smax,smin
Out[51]: (4.4, 2.0)
````
归一化公式：
```python
s = (wid - smin) / (smax - smin)
```
只打印小数点后三位设置：
```python
np.set_printoptions(precision=3)  
```

归一化结果：
```markdown
array([0.625, 0.417, 0.5  , 0.458, 0.667, 0.792, 0.583, 0.583, 0.375,
       0.458, 0.708, 0.583, 0.417, 0.417, 0.833, 1.   , 0.792, 0.625,
       0.75 , 0.75 , 0.583, 0.708, 0.667, 0.542, 0.583, 0.417, 0.583,
       0.625, 0.583, 0.5  , 0.458, 0.583, 0.875, 0.917, 0.458, 0.5  ,
       0.625, 0.458, 0.417, 0.583, 0.625, 0.125, 0.5  , 0.625, 0.75 ,
       0.417, 0.75 , 0.5  , 0.708, 0.542, 0.5  , 0.5  , 0.458, 0.125,
       0.333, 0.333, 0.542, 0.167, 0.375, 0.292, 0.   , 0.417, 0.083,
       0.375, 0.375, 0.458, 0.417, 0.292, 0.083, 0.208, 0.5  , 0.333,
       0.208, 0.333, 0.375, 0.417, 0.333, 0.417, 0.375, 0.25 , 0.167,
       0.167, 0.292, 0.292, 0.417, 0.583, 0.458, 0.125, 0.417, 0.208,
       0.25 , 0.417, 0.25 , 0.125, 0.292, 0.417, 0.375, 0.375, 0.208,
       0.333, 0.542, 0.292, 0.417, 0.375, 0.417, 0.417, 0.208, 0.375,
       0.208, 0.667, 0.5  , 0.292, 0.417, 0.208, 0.333, 0.5  , 0.417,
       0.75 , 0.25 , 0.083, 0.5  , 0.333, 0.333, 0.292, 0.542, 0.5  ,
       0.333, 0.417, 0.333, 0.417, 0.333, 0.75 , 0.333, 0.333, 0.25 ,
       0.417, 0.583, 0.458, 0.417, 0.458, 0.458, 0.458, 0.292, 0.5  ,
       0.542, 0.417, 0.208, 0.417, 0.583, 0.417])
```

**分布可视化**

```python
import seaborn as sns
sns.distplot(s,kde=False,rug=True)
```
频率分布直方图：


![](https://imgkr.cn-bj.ufileos.com/49bf5190-429c-4172-a53c-e3f6b66d4e64.png)


```python
sns.distplot(s,hist=True,kde=True,rug=True)
```
带高斯密度核函数的直方图：

![](https://imgkr.cn-bj.ufileos.com/4e4a72a5-8f59-4893-b435-e4b57e22a18e.png)



**分布 fit 图**

拿 `gamma` 分布去 fit ：
```python
from scipy import stats
sns.distplot(s, kde=False, fit = stats.gamma)
```



![](https://imgkr.cn-bj.ufileos.com/89446755-7420-4f96-97fe-c4e45d0d3dec.png)


拿双 `gamma` 去 fit：
```python
from scipy import stats
sns.distplot(s, kde=False, fit = stats.dgamma)
```

![](https://imgkr.cn-bj.ufileos.com/f2c2a660-5433-4b4f-ad7b-d01da4121319.png)

#### 17 Pandas 使用技巧

对于动辄就几十或几百个 G 的数据，在读取的这么大数据的时候，我们有没有办法随机选取一小部分数据，然后读入内存，快速了解数据和开展 EDA ？

使用 Pandas 的 skiprows 和 概率知识，就能做到。

下面解释具体怎么做。

如下所示，读取某 100 G 大小的 big_data.csv 数据

1) 使用 skiprows 参数，

2) x > 0 确保首行读入， 

3) np.random.rand() > 0.01 表示 99% 的数据都会被随机过滤掉

言外之意，只有全部数据的 1% 才有机会选入内存中。

```python
import pandas as pd
import numpy as np

df = pd.read_csv("big_data.csv", 
skiprows = 
lambda x: x>0 and np.random.rand() > 0.01)

print("The shape of the df is {}. 
It has been reduced 100 times!".format(df.shape))
```

使用这种方法，读取的数据量迅速缩减到原来的 1% ，对于迅速展开数据分析有一定的帮助。

### 十一、一步一步掌握Flask web开发

#### 1 Flask版 hello world

Flask是Python轻量级web框架，容易上手，被广大Python开发者所喜爱。

今天我们先从hello world开始，一步一步掌握Flask web开发。例子君是Flask框架的小白，接下来与读者朋友们，一起学习这个对我而言的新框架，大家多多指导。

首先`pip install Flask`,安装Flask，然后import Flask，同时创建一个 `app`
```python
from flask import Flask

App = Flask(__name__)
```

写一个index页的入口函数，返回hello world.

通过装饰器：App.route('/')创建index页的路由或地址，一个`/`表示index页，也就是主页。

```python
@App.route('/')
def index():
    return "hello world"
```

调用 `index`函数:
```python
if __name__ == "__main__":
    App.run(debug=True)
```

然后启动，会在console下看到如下启动信息，表明`服务启动成功`。
```python
* Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 663-788-611
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

 接下来，打开一个网页，相当于启动客户端，并在Url栏中输入：`http://127.0.0.1:5000/`，看到页面上答应出`hello world`，证明服务访问成功。

 同时在服务端后台看到如下信息，表示处理一次来自客户端的`get`请求。
 ```python
 27.0.0.1 - - [03/Feb/2020 21:26:50] "GET / HTTP/1.1" 200 -
 ```

 以上就是flask的hello world 版

#### 2 Flask之数据入库操作

数据持久化就是将数据写入到数据库存储的过程。

本例子使用`sqlite3`数据库。

1)导入`sqlite3`，未安装前使用命令`pip install sqlite3`

创建一个`py`文件：`sqlite3_started.py`，并写下第一行代码：
```python
import sqlite3
```
2)手动创建一个数据库实例`db`, 命名`test.db`

3)创建与数据库实例`test.db`的连接:
```python
conn = sqlite3.connect("test.db")
```

4)拿到连接`conn`的cursor
```python
c = conn.cursor()
```

5)创建第一张表`books`

共有四个字段：`id`,`sort`,`name`,`price`，类型分别为：`int`,`int`,`text`,`real`. 其中`id`为`primary key`. 主键的取值必须是唯一的(`unique`)，否则会报错。


```python
c.execute('''CREATE TABLE books
      (id int primary key,
       sort int,
       name text,
       price real)''')
```
第一次执行上面语句，表`books`创建完成。当再次执行时，就会报`重复建表`的错误。需要优化脚本，检查表是否存在`IF NOT EXISTS books`，不存在再创建：
```python
c.execute('''CREATE TABLE IF NOT EXISTS books
      (id int primary key,
       sort int,
       name text,
       price real)''')
```

6)插入一行记录

共为4个字段赋值

```python
c.execute('''INSERT INTO books VALUES
       (1, 
       1, 
       'computer science',
       39.0)''')
```

7)一次插入多行记录

先创建一个list:`books`，使用`executemany`一次插入多行。
```python
books = [(2, 2, 'Cook book', 68),
         (3, 2, 'Python intro', 89),
         (4, 3, 'machine learning', 59),
         ]


c.executemany('INSERT INTO books VALUES (?, ?, ?, ?)', books)
```

8)提交

提交后才会真正生效，写入到数据库

```python
conn.commit()
```

9)关闭期初建立的连接conn

务必记住手动关闭，否则会出现内存泄漏
```python
conn.close()
print('Done')
```

10)查看结果
例子君使用`vs code`，在扩展库中选择：`SQLite`安装。

![image-20200208211721377](./img/image-20200208211721377.png)

新建一个`sq`文件：`a.sql`，内容如下：

```sql
SELECT * from books 
```
右键`run query`，得到表`books`插入的4行记录可视化图：

![image-20200208211806853](./img/image-20200208211806853.png)

以上十步就是sqlite3写入数据库的主要步骤，作为Flask系列的第二篇，为后面的前端讲解打下基础。

#### 3 Flask各层调用关系

这篇介绍Flask和B/S模式，即浏览器/服务器模式，是接下来快速理解Flask代码的关键理论篇：**理解Views、models和渲染模板层的调用关系**。

1) 发出请求

当我们在浏览器地址栏中输入某个地址，按回车后，完成第一步。

2) 视图层 views接收1)步发出的请求，Flask中使用解释器的方式处理这个求情，实例代码如下，它通常涉及到调用models层和模板文件层

```python
@main_blue.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    print('test')
```

3) models层会负责创建数据模型，执行CRUD操作

4) 模板文件层处理html模板

5) 组合后返回html

6) models层和html模板组合后返回给views层

7）最后views层响应并渲染到浏览器页面，我们就能看到请求的页面。

完整过程图如下所示：

![image-20200211152007983](./img/web1.png)

读者朋友们，如果你和例子君一样都是初学Flask编程，需要好好理解上面的过程。理解这些对于接下来的编程会有一定的理论指导，方向性指导价值。

### Python 问答

#### Python 如何生成二维码？





## qrcode

今天先来解答如何生成二维码。Python的`qrcode`包支持生成二维码。

用法也很简单：

```python
import qrcode

# 二维码内容
data = "http://www.zglg.work/wp-content/uploads/2020/10/image-3.png"
# 生成二维码
img = qrcode.make(data=data)
# 直接显示二维码
img.show()
# 保存二维码为文件
img.save("我的微信.jpg")
```

生成的二维码如下：

![](https://imgkr2.cn-bj.ufileos.com/f0b08c53-0107-483b-bbe5-072bebc58e8d.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=rVtaeBWhzLPPq%252BFCVtiOv6rS0tI%253D&Expires=1603544615)


大家微信扫描后，会出现我的二维码。

另外，还可以设置二维码的颜色等样式：

```python
import qrcode

# 实例化二维码生成类
qr = qrcode.QRCode(border=2)
# 设置二维码数据
data = "http://www.zglg.work/wp-content/uploads/2020/10/image-3.png"
qr.add_data(data=data)
# 启用二维码颜色设置
qr.make(fit=True)
img = qr.make_image(fill_color="orange", back_color="white")

# 显示二维码
img.show()
```

生成一个orange的二维码：

![](https://imgkr2.cn-bj.ufileos.com/cbd26fd8-27cf-4630-935f-6896822ce483.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=uy1r24x%252Fp5QpI5Wy10Ebdaz%252BpLM%253D&Expires=1603544681)

更多样式，大家可以自己去玩耍。

## Python小项目：句子KWIC显示

上下文关键字（KWIC, Key Word In Context）是最常见的多行协调显示格式。

此小项目描述：输入一系列句子，给定一个给定单词，每个句子中至少会出现一次给定单词。目标输出，给定单词按照KWIC显示，KWIC显示的基本要求：待查询单词居中，前面`pre`序列右对齐，后面`post`序列左对齐，待查询单词前和后长度相等，若输入句子无法满足要求，用空格填充。

输入参数：输入句子sentences, 待查询单词selword, 滑动窗口长度`window_len`

举例，输入如下六个句子，给定单词`secure`，输出如下字符串：

```python
               pre keyword    post 

     welfare , and secure  the blessings of
     nations , and secured immortal glory with 
       , and shall secure  to you the 
    cherished . To secure  us against these 
     defense as to secure  our cities and 
          I can to secure  economy and fidelity 
```

请补充实现下面函数：

```python
def kwic(sentences: List[str], selword: str, window_len: int) -> str:
    """
    :type: sentences: input sentences
    :type: selword: selected word
    :type: window_len: window length
    """
```

更多KWIC显示参考如下：

http://dep.chs.nihon-u.ac.jp/english_lang/tukamoto/kwic_e.html

完整代码已经公布在：http://www.zglg.work/Python-20-topics/python-project1-kwic/
![image](https://user-images.githubusercontent.com/20391209/123213609-c494dc00-d4f8-11eb-84d6-4d8caabb44f7.png)
![image](https://user-images.githubusercontent.com/20391209/123213901-26eddc80-d4f9-11eb-96cd-d3518005c4df.png)

