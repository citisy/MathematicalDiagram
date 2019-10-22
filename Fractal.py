"""http://www.matrix67.com/blog/archives/6231#more-6231"""

import turtle


def koch_curve(length=2, depth=5):
    def recursion(length, depth=0):
        if depth == 0:
            turtle.fd(length)
        else:
            recursion(length, depth - 1)
            turtle.lt(60)
            recursion(length, depth - 1)
            turtle.rt(120)
            recursion(length, depth - 1)
            turtle.lt(60)
            recursion(length, depth - 1)

    # 设置原点为屏幕中心
    turtle.pu()
    turtle.goto(-length * 3 ** depth / 2, length * 3 ** depth / 2 / 3 ** 0.5)
    turtle.pd()

    for _ in range(3):
        recursion(length, depth)
        turtle.rt(120)


def pythagoras_tree(point0=(-50, -200), point1=(50, -200), depth=10):
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
    recursion(*point0, *point1, depth=depth)


def dragon_curve(length=2, depth=14):
    """http://blog.sciencenet.cn/blog-677221-601957.html

    main process:
    2nd recursion: r r l
    3rd recursion: rrl r rll
    4th recursion: rrlrrll r rrllrll
    ......

    right part and left part, it's symmetric"""

    def recursion_right(length, depth):
        if depth == 0:
            turtle.fd(length)
        else:
            recursion_right(length, depth - 1)
            turtle.rt(90)
            recursion_left(length, depth - 1)

    def recursion_left(length, depth):
        if depth == 0:
            turtle.fd(length)
        else:
            recursion_right(length, depth - 1)
            turtle.lt(90)
            recursion_left(length, depth - 1)

    recursion_right(length, depth)


def sierpinski_triangle(length=0.5, depth=5):
    def recursion(length, flag=1, depth=0):
        if depth == 0:
            turtle.fd(length)
        else:
            recursion(length, flag, depth - 1)
            turn(flag)
            recursion(length, -flag, depth - 1)
            turn(flag)
            recursion(length, flag, depth - 1)
            turn(-flag)
            recursion(length, -flag, depth - 1)
            turn(-flag)
            recursion(length, flag, depth - 1)
            turn(-flag)
            recursion(length, -flag, depth - 1)
            turn(-flag)
            recursion(length, flag, depth - 1)
            turn(flag)
            recursion(length, -flag, depth - 1)
            turn(flag)
            recursion(length, flag, depth - 1)

    def turn(flag):
        if flag == 1:
            turtle.lt(60)
        else:
            turtle.rt(60)

    # 设置原点为屏幕中心
    turtle.pu()
    turtle.goto(-length * 4 ** depth / 2, -length * 4 ** depth / 2 / 3 ** 0.5)
    turtle.pd()

    recursion(length, 1, depth)


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

    sierpinski_triangle()

    turtle.tracer(True)
    turtle.done()
