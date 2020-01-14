from utils import *
import turtle


def koch_curve(length=2, depth=5, save_path=None):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 60
    start_point = (-length * 3 ** depth / 2, length * 3 ** depth / 2 / 3 ** 0.5)

    paint_fractal({'s': 'f++f++f', 'f': 'f-f++f-f'},
                  angle, length, depth, start_point=start_point, save_path=save_path)


def dragon_curve(length=2, depth=14, save_path=None):
    """http://blog.sciencenet.cn/blog-677221-601957.html

    main process:
    2nd recursion: r r l
    3rd recursion: rrl r rll
    4th recursion: rrlrrll r rrllrll
    ......

    right part and left part, it's symmetric"""

    angle = 90
    start_point = ()
    paint_fractal({'s': 'fr', 'r': 'r+lf+', 'l': '-fr-l'},
                  angle, length, depth, save_path=save_path)


def pythagoras_tree(p0=(-50, -200), p1=(50, -200), depth=10):
    """p0, p1: left bottom point and right bottom point of square"""

    def recursion(x0, y0, x1, y1, depth=0):
        if depth > 0:
            dx, dy = x1 - x0, y1 - y0
            x2, y2 = x1 - dy, y1 + dx
            x3, y3 = x0 - dy, y0 + dx
            x4, y4 = x3 + (dx - dy) / 2, y3 + (dx + dy) / 2

            t.goto(x0, y0)
            t.begin_fill()
            t.pendown()  # 画笔放下

            for x, y in ((x1, y1), (x2, y2), (x3, y3), (x0, y0)):  # 正方形的四个顶点
                t.goto(x, y)

            t.penup()  # 画笔提起
            t.end_fill()
            recursion(x3, y3, x4, y4, depth - 1)
            recursion(x4, y4, x2, y2, depth - 1)

    t = turtle.Turtle()
    t.hideturtle()

    t.color('blue', 'blue')
    t.penup()
    recursion(*p0, *p1, depth=depth)


def sierpinski_triangle(p0=(-250, -200), p1=(250, -200), depth=6):
    """p0, p1: left bottom point and right bottom point of triangle"""

    def recursion(p0, p1, p2, depth=0):
        if depth == 0:
            t.penup()
            t.goto(p0)
            t.pendown()
            t.begin_fill()
            for p in (p1, p2, p0):
                t.goto(p)
            t.end_fill()
        else:
            (x0, y0), (x1, y1), (x2, y2) = p0, p1, p2
            p01 = ((x0 + x1) / 2, (y0 + y1) / 2)
            p02 = ((x0 + x2) / 2, (y0 + y2) / 2)
            p12 = ((x1 + x2) / 2, (y1 + y2) / 2)

            recursion(p0, p01, p02, depth - 1)
            recursion(p1, p01, p12, depth - 1)
            recursion(p2, p02, p12, depth - 1)

    (x0, y0), (x1, y1) = p0, p1
    length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    t = np.pi / 3
    cost, sint = abs(x1 - x0) / length, abs(y1 - y0) / length
    sint_, cost_ = sin(t) * cost - cos(t) * sint, cos(t) * cost + sin(t) * sint
    p2 = (x0 + length * cost_, y0 + length * sint_)

    t = turtle.Turtle()
    t.penup()
    t.goto(p0)
    t.pendown()

    for p in (p1, p2, p0):
        t.goto(p)

    t.color('blue', 'blue')
    recursion(p0, p1, p2, depth=depth)


def sierpinski_triangle2(length=0.5, depth=5, save_path=None):
    angle = 60
    start_point = (-length * 4 ** depth / 2, -length * 4 ** depth / 2 / 3 ** 0.5)
    paint_fractal({'s': 'F', 'F': 'F-f-F+f+F+f+F-f-F', 'f': 'f+F+f-F-f-F-f+F+f'},
                  angle, length, depth, start_point=start_point, save_path=save_path)


def sierpinski_triangle3(length=2, depth=7, save_path=None):
    angle = 60
    start_point = ()
    paint_fractal({'s': 'f', 'f': 'F-f-F', 'F': 'f+F+f'},
                  angle, length, depth, save_path=save_path)


def sierpinski(length=5, depth=10, save_path=None):
    angle = 45
    strat_point = ()
    paint_fractal({'s': 'l--f--l--f', 'l': '+r-f-r+', 'r': '-l+f+l-'},
                  angle, length, depth, save_path=save_path)


def lvey_c(length=2, depth=14, save_path=None):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 45
    start_point = (-length * 2 ** (depth / 2 - 1), length * 2 ** (depth / 2 - 2))
    paint_fractal({'s': 'f', 'f': '+f--f+'},
                  angle, length, depth, start_point=start_point, save_path=save_path)


def hilbert(length=10, depth=5, save_path=None):
    angle = 90
    strat_point = ()
    paint_fractal({'s': 'r', 'r': '-lf+rfr+fl-', 'l': '+rf-lfl-fr+'},
                  angle, length, depth, save_path=save_path)


def leaf(length=2, depth=6, save_path=None):
    angle = 25
    strat_point = ()
    paint_fractal({'s': 'x', 'x': 'f-[[x]+x]+f[+fx]-x', 'f': 'ff'},
                  angle, length, depth, start_angle=-45, save_path=save_path)


if __name__ == '__main__':
    turtle.tracer(False)

    pythagoras_tree()

    turtle.tracer(True)
    turtle.done()

    # depth = 6
    # leaf(depth=depth, save_path='fractal/leaf%d.png' % depth)
