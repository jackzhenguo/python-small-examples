import turtle
import random
import time


class MyTurtle(turtle.Turtle):
    '''
    # MyTurtle 类
    + ## get_color() 
    > ### 随机取rgb模式下的颜色的三个参数
    + ## set_pen_color() 
    > ### 设置画笔使用颜色
    + ## move(x, y) 
    > ### 控制海龟移动到指定x,y坐标(移动轨迹不着色)
    + ## draw_shape(sides, length)
    > ### 画 sides 条边，length 长度的图形
    + ## draw_square(length)
    > ### 调用 draw_shape() 函数画边长为 length 正方形
    + ## draw_triangle(length)
    > ### 调用 draw_shape() 函数画边长为 length 等边三角形
    + ## draw_circle(length)
    > ### 调用 draw_shape() 函数画半径为 length 圆形
    + ## fill_color_shape(shape, length, fill_color)
    > ### 用 fill_color 颜色, 填充 length 边长, shape （draw_square, draw_triangle, draw_circle）设定的图形


    ## turtle 函数介绍
    + ### left(x)/right(x)                      
    > 使海龟 逆时针/顺时针 旋转
    + ### circle(x)
    > 以x为半径，以当前方向开始画圆
    + ### forward(x)|fd(x)                      
    > 前进x，单位为像素
    + ### backward(x)|bk(x)|back(x)             
    > 后退x，单位为像素
    + ### goto(x,y)|setpos(x,y)|setposition(x,y)
    > 使海龟沿直线移动到(x,y)坐标处
    + ### setx(x)/sety(y)                       
    > 设置 x/y 坐标，使海龟水平移动
    + ### dot(size,color)                       
    > 在当前位置以直径为size画点，颜色为color
    + ### speed(n)                              
    > 设置海龟的移动速度
    + ### pendown()|pd()|down()                 
    > 使海龟“落地”，移动轨迹在屏幕上显示
    + ### penup()|up()                          
    > 使海龟“起飞”,移动轨迹在屏幕上不显示
    + ### pensize(x)                            
    > 设置画笔宽度为x，单位为像素
    + ### pencolor(color)                       
    > 设置画笔颜色
    + ### fillcolor()                           
    > 设置填充颜色，当轨迹形成闭合图形时填充的颜色
    + ### begin_fill()/end_fill()               
    > 控制颜色填充的时间段，只有在begin_fill()与end_fill()中间的闭合图形才会填充颜色
    '''

    def get_color(self):
        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))
        return rgb

    def set_pen_color(self):
        '''
        ## 设置画笔的颜色
        + ### colormode(cmode) 
        >- cmode 为1 或者 255， 
        >- 随后rgb三元组的值必须在0~comde之间
        + ### pencolor(color=None) 
        > 设置画笔颜色
        '''
        self.screen.colormode(255)
        self.pencolor(self.get_color())

    def move(self, x: int, y: int) -> None:
        self.penup()
        self.goto(x, y)
        self.pendown()

    def draw_shape(self, sides: int, length: int) -> None:
        _angle = 360.0/sides
        for side in range(sides):
            self.forward(length)
            self.left(_angle)

    def draw_square(self, length: int) -> None:
        self.draw_shape(4, length)

    def draw_triangle(self, length: int) -> None:
        self.draw_shape(3, length)

    def draw_circle(self, length: int) -> None:
        self.draw_shape(360, length)

    def fill_color_shape(self, shape: str, length: int, fill_color: str) -> None:
        _command = f'self.{shape}(length)'
        self.begin_fill()
        self.color(fill_color)
        eval(_command)
        self.end_fill()


def diff_color_square_address(star: list, end: int, step: int) -> list:
    '''
    根据 star 列表（通常为[x, y]起始坐标）， end 坐标最大值，step 步长，来计算出所有坐标
    返回坐标列表（[[x,y], [x, y1], [x1, y], [x1, y1], ...]） 
    '''
    x = list(range(star[0], end+1, step))
    y = list(range(star[1], end+1, step))
    res_array = []
    for xi in x:
        for yi in y:
            res_array.append([xi, yi])
    return res_array


def draw_main(b_val: int, s_len: int) -> None:
    '''
    + ### bgcolor(color) 
    > 设置屏幕颜色，方式同 color()
    + ### speed(s=None) 
    > s为0-10的整数或者速度字符串
        - None：返回当前速度
        - "fastest"：0
        - "fast"：10
        - "normal"：6
        - "slow"：3
        - "slowest"：1
    '''
    star_time = time.time()
    t = MyTurtle()

    t.screen.bgcolor("black")  # white
    t.speed(100)

    tem_b = b_val + 1
    tem_s = b_val - tem_b % 2  # 取单数数量
    sx = list(x1 for x1 in range(1, tem_s))  # 小方格基本坐标
    sy = list(y1 for y1 in range(1, tem_s))
    bx = list(x1 for x1 in range(1, tem_b))  # 大方格基本坐标
    by = list(y1 for y1 in range(1, tem_b))

    b_len = len(sx)  # 大方格边长
    different_colors_square_list = [
        diff_color_square_address([2, 2], b_val, 4),  # 混合橙色坐标
        diff_color_square_address([4, 4], b_val, 4),  # 混合淡绿色坐标
        diff_color_square_address([4, 2], b_val, 4),  # 混合紫色坐标
        diff_color_square_address([2, 4], b_val, 4)  # 混合绿松石色坐标
    ]

    color_list = [
        ['red', 'yellow'],  # 混合橙色
        ['green', 'yellow'],  # 混合淡绿色
        ['red', 'blue'],    # 混合紫色
        ['green', 'blue'],  # 混合绿松石色
        ['yellow', 'blue'],  # 混合灰色
    ]

    offset = (s_len * b_len * (b_val + 2) + s_len) / 2
    print(
        f's_len: {s_len}, b_len: {b_len}, offset: {offset}, turtle: {t._screen.screensize()}')
    turtle.tracer(False)  # 如果想看看程序的画图过程设成True
    for x3 in bx:
        for y3 in by:
            for x4 in sx:
                for y4 in sy:
                    x = x3 * s_len * b_len + x4 * s_len - offset
                    y = y3 * s_len * b_len + y4 * s_len - offset
                    t.move(int(x), int(y))
                    # 判断坐标是否在特定颜色组坐标中，是选用对应颜色组
                    if [x3, y3] in different_colors_square_list[0]:
                        colors = color_list[0]
                    elif [x3, y3] in different_colors_square_list[1]:
                        colors = color_list[1]
                    elif [x3, y3] in different_colors_square_list[2]:
                        colors = color_list[2]
                    elif [x3, y3] in different_colors_square_list[3]:
                        colors = color_list[3]
                    else:
                        colors = color_list[4]

                    if ((x4 + y4) % 2) == 0:
                        color = colors[0]
                    else:
                        color = colors[1]
                    t.fill_color_shape('draw_square', s_len, color)
    t.move(800, 800)
    turtle.update()
    end_time = time.time() - star_time
    # print_time = time.strftime("%b %d %Y %H:%M:%S", end_time)
    print(end_time)
    t.screen.mainloop()


if __name__ == '__main__':
    big_input = 9
    big_value = 9 if big_input == '' or int(big_input) <= 0 else int(big_input)
    small_input = 5
    small_len = 5 if small_input == '' or int(
        small_input) <= 0 else int(small_input)
    print('big_value:', big_value, type(big_value),
          '\n', 'small_len:', small_len, type(small_len))
    draw_main(big_value, small_len)
