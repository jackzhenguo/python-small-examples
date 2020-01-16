import matplotlib.pyplot as plt
import turtle as p

lat = [
    30.42642,
    30.40874,
    30.41054,
    30.33076,
    30.34913,
    30.37498,
    30.37501,
    30.37501,
    30.37501,
    30.37651,
    30.37399,
    30.3823,
    30.39114,
    30.40265,
    30.429,
    30.43278,
    30.28439,
    30.28439,
    30.28439,
    30.28379
]

lng = [
    103.99214,
    103.98516,
    103.98321,
    103.95224,
    104.03915,
    104.05311,
    104.05316,
    104.05316,
    104.05316,
    104.05576,
    104.05416,
    104.16558,
    104.17339,
    104.14988,
    104.20051,
    104.20075,
    104.11849,
    104.11849,
    104.11849,
    104.12141
]

begin_lat_lng = (30.63572, 103.92430)

# p.pu()  # 抬起画笔
# p.goto(begin_lat_lng)  # 起始位置
# p.color('red')  # 绘制
# p.pensize(3)  # 画笔尺寸设置3
# for x, y in zip(lat, lng):
#     p.pd()  # 放下画笔
#     p.goto(x, y)
#     p.pu()
#     print(x, y)


# p.done()
lat.insert(0, begin_lat_lng[0])
lng.insert(0, begin_lat_lng[1])

plt.plot(lat, lng)
plt.scatter(lat[0], lng[0], c='r')
plt.scatter(lat[1:], lng[1:], c='b')
for i in range(len(lat)):
    plt.text(lat[i], lng[i], str(i))

plt.show()
