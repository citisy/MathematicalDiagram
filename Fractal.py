"""http://www.matrix67.com/blog/archives/6231#more-6231"""

import turtle


def koch_curve():
    def recursion(length, depth=0):
        if depth == 0:
            turtle.fd(length)
        else:
            recursion(length / 3, depth - 1)
            turtle.lt(60)
            recursion(length / 3, depth - 1)
            turtle.rt(120)
            recursion(length / 3, depth - 1)
            turtle.lt(60)
            recursion(length / 3, depth - 1)

    def painter(length, depth):
        for _ in range(3):
            recursion(length, depth)
            turtle.rt(120)

    length = 300

    # 设置原点为屏幕中心
    turtle.pu()
    turtle.goto(-length / 2, length / 2 / 3 ** 0.5)
    turtle.pd()

    painter(length, depth=5)


def pythagoras_tree():
    def recursion(x0, y0, x1, y1, depth=0):
        if depth > 0:
            dx, dy = x1 - x0, y1 - y0
            x2, y2 = x1 - dy, y1 + dx
            x3, y3 = x0 - dy, y0 + dx
            x4, y4 = x3 + (dx - dy) / 2, y3 + (dx + dy) / 2

            turtle.goto(x0, y0)
            turtle.begin_fill()
            turtle.pd()  # 画笔放下

            for x, y in ((x1, y1), (x2, y2), (x3, y3), (x0, y0)):
                turtle.goto(x, y)

            turtle.pu()  # 画笔提起
            turtle.end_fill()
            recursion(x3, y3, x4, y4, depth - 1)
            recursion(x4, y4, x2, y2, depth - 1)

    turtle.color('blue', 'blue')
    turtle.pu()
    recursion(-50, -200, 50, -200, depth=10)


def dragon_curve():
    """http://blog.sciencenet.cn/blog-677221-601957.html"""

    # def recursion(length, depth=0):
    #     if depth == 0:
    #         turtle.fd(length)
    #     else:
    #         turtle.lt(45)
    #         recursion(length / 2 ** 0.5, depth - 1)
    #         turtle.rt(90)
    #         recursion(length / 2 ** 0.5, depth - 1)
    #
    # recursion(length=400, depth=3)
    def dragon_right(max_len, min_len):
        '''draw lines favoring right'''
        # optionally draw this part in red
        turtle.color('red')
        if max_len <= min_len:
            turtle.forward(max_len)
        else:
            max_len /= 2.0
            # print(max_len)  # test
            dragon_right(max_len, min_len)
            turtle.right(90)
            dragon_left(max_len, min_len)

    def dragon_left(max_len, min_len):
        '''draw lines favoring left'''
        # optionally draw this part in blue
        turtle.color('blue')
        if max_len <= min_len:
            turtle.forward(max_len)
        else:
            max_len /= 2.0
            # print(max_len)  # test
            dragon_right(max_len, min_len)
            turtle.left(90)
            dragon_left(max_len, min_len)

    def dragon_curve(max_len, min_len, color):
        dragon_right(max_len, min_len)

    max_len = 4000
    min_len = 30


def spiral():
    turtle.bgcolor('black')
    colors = ['red', 'yellow', 'purple', 'blue']

    for x in range(400):
        turtle.forward(2 * x)
        turtle.color(colors[x % 4])
        turtle.left(91)


if __name__ == '__main__':
    turtle.ht()
    turtle.speed('fastest')
    turtle.tracer(False)

    dragon_curve()

    turtle.tracer(True)
    turtle.done()
