import numpy as np
from numpy import sin, cos, pi, exp, tan
# from sympy import sin, cos, pi, exp
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.colors as colors
import mpl_toolkits.mplot3d
from tqdm import tqdm

normal = 0
polar = 1


def painter(ax, fig, draw_args=dict()):
    ax.set_xlim(*draw_args.get('xlim', ax.get_xlim()))
    ax.set_ylim(*draw_args.get('ylim', ax.get_ylim()))
    ax.set_title(draw_args.get('title', ''))

    if not draw_args.get('axis', False):
        ax.set_axis_off()

    fig.set_facecolor(draw_args.get('facecolor', 'papayawhip'))
    ax.set_facecolor(draw_args.get('facecolor', 'papayawhip'))

    if draw_args.get('save_path', None) is not None:
        plt.savefig(draw_args.get('save_path'), facecolor=fig.get_facecolor())

    if draw_args.get('show_fig', True):
        plt.show()


def implicit_formulae_painter(xaxis=None, yaxis=None,
                              axis_type=normal, taxis=None, raxis=None,
                              steps=2 ** 10,
                              func=None, draw_args=dict()):
    """`f(x, y) = 0` 类型函数作图
    2维扩展至3维，做等高线，调用了matplotlib的contour函数"""
    if axis_type == polar:
        xaxis, yaxis = taxis, raxis

    x = np.linspace(*xaxis, steps)
    y = np.linspace(*yaxis, steps)
    xx, yy = np.meshgrid(x, y)
    zz = func(xx, yy)

    if axis_type == polar:
        xx, yy = yy * cos(xx), yy * sin(xx)

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()
    ax.contour(xx, yy, zz, 0, colors=draw_args.get('color', 'r'))

    painter(ax, fig, draw_args)

    return ax, (xx, yy, zz)


def implicit_formulae_painter2(xaxis=None, yaxis=None,
                               axis_type=normal, taxis=None, raxis=None,
                               steps=2 ** 10,
                               func=None, draw_args=dict()):
    """`f(x, y) = 0` 类型函数作图
    隐函数求解，调用了sympy的plot_implicit函数
    todo: 极坐标系是图像会出错"""
    from sympy import symbols, plot_implicit

    if axis_type == polar:
        xaxis, yaxis = taxis, raxis

    x, y = symbols('x y')
    z = func(x, y)

    p = plot_implicit(z, (x, *xaxis), (y, *yaxis),
                      points=steps, line_color=draw_args.get('color', 'r'), show=False,
                      xlim=draw_args.get('xlim', (None, None)), ylim=draw_args.get('ylim', (None, None)),
                      title=draw_args.get('title', ''))

    if draw_args.get('save_path', None) is not None:
        p.save(draw_args.get('save_path'))

    p.show()


def implicit_formulae_painter3(xaxis=None, yaxis=None,
                               axis_type=normal, taxis=None, raxis=None,
                               steps=1000, k=1.,
                               func=None, draw_args=dict(), **kwargs):
    """`f(x, y) = 0` 类型函数作图
    梯度求解法"""
    if axis_type == polar:
        xaxis, yaxis = taxis, raxis

    x = np.linspace(*xaxis, steps)
    y = np.linspace(*yaxis, steps)
    xx, yy = np.meshgrid(x, y)
    zz = func(xx, yy)

    grad = np.gradient(zz)
    mold = np.sqrt(grad[0] ** 2 + grad[1] ** 2)
    zz = np.abs(zz)

    a = zz < k * mold
    a = a[::-1, :]

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    cmap = colors.ListedColormap([draw_args.get('facecolor', 'papayawhip'), 'red'])
    ax.imshow(a, cmap=cmap)

    painter(ax, fig, draw_args)


def implicit_formulae_painter4(xaxis=None, yaxis=None,
                               axis_type=normal, taxis=None, raxis=None,
                               steps=1000,
                               func=None, draw_args=dict(), **kwargs):
    """`f(x, y) = 0` 类型函数作图
    Marching squares 算法"""
    if axis_type == polar:
        xaxis, yaxis = taxis, raxis

    x = np.linspace(*xaxis, steps)
    y = np.linspace(*yaxis, steps)
    xx, yy = np.meshgrid(x, y)
    zz = func(xx, yy)

    if axis_type == polar:
        x, y = y * cos(x), y * sin(x)

    r = np.zeros_like(zz, dtype=int)
    r[zz > 0] = 1

    mask = np.zeros((4, r.shape[0], r.shape[1]), dtype=int)
    mask[0], mask[1], mask[2], mask[3] = 2, 3, 4, 5
    mask = mask * r

    w = np.zeros((4, r.shape[0] - 1, r.shape[1] - 1), dtype=int)
    w[0], w[1], w[2], w[3] = mask[0][:-1, :-1], mask[1][:-1, 1:], mask[2][1:, :-1], mask[3][:-1, :-1]
    w[w == 0] = 1

    sites = np.prod(w, axis=0)

    middle_x, middle_y = (x[:-1] + x[1:]) / 2, (y[:-1] + y[1:]) / 2

    site_map = {
        2 : [[0, 3]],
        3 : [[0, 1]],
        4 : [[2, 3]],
        5 : [[1, 2]],
        6 : [[1, 3]],
        8 : [[0, 2]],
        10: [[0, 1], [2, 3]],
        12: [[0, 3], [1, 2]],
        15: [[0, 2]],
        20: [[1, 3]],
        24: [[1, 2]],
        30: [[2, 3]],
        40: [[0, 1]],
        60: [[0, 3]],
    }

    lines = []

    for i in range(r.shape[1] - 1):
        for j in range(r.shape[0] - 1):
            site = sites[j, i]

            if site == 1 or site == 120:
                continue

            point_map = [(middle_x[i], y[j]),
                         (x[i + 1], middle_y[j]),
                         (middle_x[i], y[j + 1]),
                         (x[i], middle_y[j])]

            points = site_map[site]

            for point in points:
                lines.append([point_map[point[0]], point_map[point[1]]])

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    lc = collections.LineCollection(lines, colors=draw_args.get('color', 'r'))
    ax.add_collection(lc, autolim=True)
    ax.autoscale_view()

    painter(ax, fig, draw_args)


def implicit_formulae_painter5(xaxis=None, yaxis=None,
                               axis_type=normal, taxis=None, raxis=None,
                               steps=1000,
                               func=None, draw_args=dict(), **kwargs):
    """`f(x, y) = 0` 类型函数作图
    todo: Tupper interval arithmetic"""


def explicit_formulae_painter(axis_type: int = normal,
                              axis_list: iter = None,
                              steps: int = 2 ** 10,
                              func=None,
                              draw_args: dict = dict(),
                              **kwargs):
    """`y = f(x)` 类型函数作图

    Parameters
    ----------
    axis_type
        绘图坐标系，默认直角坐标系，值为polar时为极坐标系
    axis_list
        x的取值区间列表
    steps
        每个区间的作图的像素
    func
        函数表达式
    draw_args
        作图参数
    """
    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    for axis in axis_list:
        x = np.linspace(*axis, steps)
        y = func(x)
        if axis_type == polar:
            x, y = y * cos(x), y * sin(x)

        ax.plot(x, y, c=draw_args.get('color', 'r'), linewidth=draw_args.get('linewidth', 2))

    painter(ax, fig, draw_args)


def transform_formulae_painter(taxis_list=None, axis_type=normal, steps=2 ** 10,
                               func=None, draw_args=dict()):
    """`x = f(t), y = f(t)` 类型函数作图"""

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    for taxis in taxis_list:
        t = np.linspace(*taxis, steps)
        x, y = func(t)
        if axis_type == polar:
            x, y = y * cos(x), y * sin(x)

        ax.plot(x, y, c=draw_args.get('color', 'r'))

    painter(ax, fig, draw_args)


def get_path(rule, depth):
    path = rule['s']

    for i in range(depth):
        current_path = []
        for p in path:
            if p in rule:
                current_path.append(rule[p])
            else:
                current_path.append(p)
        path = "".join(current_path)

    return path


def fractal_painter_with_plt(rule, angle, length, depth, start_angle=None,
                             draw_args=dict(), **kwargs):
    """分形作图
    调用matplotlib绘图"""
    path = get_path(rule, depth)

    p = (0.0, 0.0)
    start_angle = start_angle or 0
    lines = []
    stack = []
    for c in path:
        if c == 'F':
            r = start_angle * pi / 180
            t = p[0] + length * cos(r), p[1] + length * sin(r)
            lines.append(((p[0], p[1]), (t[0], t[1])))
            p = t
        elif c == 'f':
            r = start_angle * pi / 180
            t = p[0] + length * cos(r), p[1] + length * sin(r)
            p = t
        elif c == '+':
            start_angle += angle
        elif c == '-':
            start_angle -= angle
        elif c == '[':
            stack.append((p, start_angle))
        elif c == ']':
            p, start_angle = stack.pop(-1)

    fig, ax = plt.subplots()

    lc = collections.LineCollection(lines)
    ax.add_collection(lc, autolim=True)
    ax.axis("equal")
    ax.invert_yaxis()

    painter(ax, fig, draw_args)


def fractal_painter_with_turtle(rule, angle, length, depth, start_point=None, start_angle=None,
                                draw_args=dict(), **kwargs):
    """分形作图
    调用turtle绘图"""
    import turtle

    path = get_path(rule, depth)

    t = turtle.Turtle()
    screen = turtle.Screen()

    t.hideturtle()
    t.speed('fastest')
    screen.tracer(False)

    if start_point is not None:
        t.penup()
        t.goto(start_point)
        t.pendown()

    if start_angle is not None:
        t.penup()
        t.setheading(start_angle)
        t.pendown()

    cache = []
    for p in path:
        if p == 'F':
            t.forward(length)
        elif p == 'f':
            t.penup()
            t.forward(length)
            t.pendown()
        elif p == '-':
            t.left(angle)
        elif p == '+':
            t.right(angle)
        elif p == '[':
            cache.append((t.pos(), t.heading()))
        elif p == ']':
            cache_p, cache_a = cache.pop(-1)
            t.penup()
            t.goto(cache_p)
            t.setheading(cache_a)
            t.pendown()

    screen.tracer(True)
    screen.bgcolor(draw_args.get('facecolor', 'papayawhip'))
    screen.mainloop()


def fractal_painter_with_tkinter(rule, angle, length, depth, start_point=None, start_angle=None,
                                 draw_args=dict(), **kwargs):
    """分形作图
    调用tkinter绘图"""
    import tkinter

    path = get_path(rule, depth)

    width, height = 1024, 768

    tk = tkinter.Tk()
    canvas = tkinter.Canvas(tk, width=1024, height=768,
                            bg=draw_args.get('facecolor', 'papayawhip'))
    canvas.pack()

    p = (height / 2, width / 2)
    start_angle = start_angle or 0
    stack = []
    for c in path:
        if c == 'F':
            r = start_angle * pi / 180
            t = p[0] + length * cos(r), p[1] + length * sin(r)
            canvas.create_line(p[0], p[1], t[0], t[1])
            p = t
        elif c == 'f':
            r = start_angle * pi / 180
            t = p[0] + length * cos(r), p[1] + length * sin(r)
            p = t
        elif c == '+':
            start_angle += angle
        elif c == '-':
            start_angle -= angle
        elif c == '[':
            stack.append((p, start_angle))
        elif c == ']':
            p, start_angle = stack.pop(-1)

    tk.mainloop()


def chaos_fractal_painter(xs, ys, draw_args=dict()):
    """混沌分形作图"""
    fig = plt.figure(figsize=draw_args.get('figsize', (8, 8)))
    ax = fig.add_subplot()

    ax.scatter(xs, ys, s=1, marker=',')

    painter(ax, fig, draw_args)


def attractor_painter(func, *args, dt=0.001, n_steps=100000, start_xyz=(0.1, 0.1, 0.1),
                      save_path=None, **kwargs):
    """吸引子作图"""
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)
    zs = np.zeros(n_steps + 1)

    xs[0], ys[0], zs[0] = start_xyz

    for i in range(n_steps):
        if args:
            (dx, dy, dz), d = func(xs[i], ys[i], zs[i], *args)
            args = tuple(args[i] + d[i] for i in range(len(args)))
        else:
            dx, dy, dz = func(xs[i], ys[i], zs[i])

        xs[i + 1] = xs[i] + (dx * dt)
        ys[i + 1] = ys[i] + (dy * dt)
        zs[i + 1] = zs[i] + (dz * dt)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot(xs, ys, zs, linewidth=.5)

    painter(ax, fig, draw_args={'save_path': save_path})
