import numpy as np
from numpy import sin, cos, pi
# from sympy import sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

normal = 0
polar = 1


def painter(ax, fig, draw_args=dict()):
    plt.xlim(*draw_args.get('xlim', (None, None)))
    plt.ylim(*draw_args.get('ylim', (None, None)))
    plt.title(draw_args.get('title', ''))

    ax.set_axis_off()
    fig.set_facecolor('papayawhip')
    ax.set_facecolor('papayawhip')

    if draw_args.get('save_path', None) is not None:
        plt.savefig(draw_args.get('save_path'), facecolor=fig.get_facecolor())

    plt.show()


def implicit_formulae_painter(xaxis=None, yaxis=None,
                              axis_type=normal, taxis=None, raxis=None,
                              steps=2 ** 10,
                              func=None, draw_args=dict()):
    """f(x, y) = 0
    2维扩展至3维，做等高线，调用了matplotlib的contour函数"""
    if axis_type == polar:
        xaxis, yaxis = taxis, raxis

    x = np.linspace(*xaxis, steps)
    y = np.linspace(*yaxis, steps)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    if axis_type == polar:
        X, Y = Y * np.cos(X), Y * np.sin(X)

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()
    ax.contour(X, Y, Z, 0, colors=draw_args.get('color', 'r'))
    painter(ax, fig, draw_args)


def implicit_formulae_painter2(xaxis=None, yaxis=None,
                               axis_type=normal, taxis=None, raxis=None,
                               steps=2 ** 10,
                               func=None, draw_args=dict()):
    """f(x, y) = 0
    隐函数求解，调用了sympy的plot_implicit"""
    from sympy import symbols, plot_implicit

    x, y = symbols('x y')
    p = plot_implicit(func(x, y), (x, *xaxis), (y, *yaxis),
                      points=steps, line_color=draw_args.get('color', 'r'), show=False,
                      xlim=draw_args.get('xlim', (None, None)), ylim=draw_args.get('ylim', (None, None)),
                      title=draw_args.get('title', ''))

    if draw_args.get('save_path', None) is not None:
        p.save(draw_args.get('save_path'))

    p.show()


def implicit_formulae_painter3(xaxis=None, yaxis=None, axis_type=normal, taxis=None, raxis=None, steps=2 ** 5,
                               func=None, draw_args=dict(), **kwargs):
    """f(x, y) = 0
    todo: 二分描点，部分算法尚未完成"""

    def recursion(start_xx, start_yy, start_set, batch_steps, steps, eps, func):
        step_width = (start_xx[1] - start_xx[0], start_yy[1] - start_yy[0])
        result = np.zeros((steps * batch_steps, steps * batch_steps), dtype=np.int8)

        for idn in tqdm(start_set):
            idx, idy = idn[0], idn[1]

            xx = np.linspace(start_xx[idx], start_xx[idx] + step_width[0], batch_steps)
            yy = np.linspace(start_yy[idy], start_yy[idy] + step_width[1], batch_steps)

            for i, x in enumerate(xx):
                for j, y in enumerate(yy):
                    r = func(x, y)
                    if type(r) is list:
                        r = any([abs(_) < eps for _ in r])
                    elif type(r) is np.float64:
                        r = abs(r) < eps

                    if r:
                        result[idx * 2 + i][idy * 2 + j] = 1

        border_set = set()
        index = np.where(result == 1)
        for a in range(index[0].size):
            border_set.add(tuple([index[0][a], index[1][a]]))

        return border_set

    if axis_type == polar:
        axis1, axis2 = taxis, raxis
    else:
        axis1, axis2 = xaxis, yaxis

    eps = kwargs.get('eps', 2 ** 1)
    iterate = kwargs.get('iterate', 7)
    batch_steps = 2
    start_set = set()

    for i in range(steps):
        for j in range(steps):
            start_set.add(tuple([i, j]))  # start border

    for _ in range(iterate):
        xx = np.linspace(*axis1, steps)
        yy = np.linspace(*axis2, steps)

        start_set = recursion(xx, yy, start_set, batch_steps, steps, eps, func)

        steps *= 2
        eps /= 2

    xs, ys = [], []
    xx = np.linspace(*axis1, steps)
    yy = np.linspace(*axis2, steps)

    for idn in start_set:
        x, y = xx[idn[0]], yy[idn[1]]
        if axis_type == polar:
            xs.append(y * np.cos(x))
            ys.append(y * np.sin(x))
        else:
            xs.append(x)
            ys.append(y)

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    ax.scatter(xs, ys, s=1, c=draw_args.get('color', 'r'), marker=',')
    painter(ax, fig, draw_args)


def explicit_formulae_painter(xaxis_list=None, axis_type=normal, taxis_list=None,
                              steps=2 ** 10, func=None, draw_args=dict()):
    """y = f(x)"""
    if axis_type == polar:
        axis_list = taxis_list
    else:
        axis_list = xaxis_list

    xs, ys = [], []
    for axis in axis_list:
        for x in tqdm(np.linspace(*axis, steps)):
            y = func(x)
            if axis_type == polar:
                xs.append(y * np.cos(x))
                ys.append(y * np.sin(x))
            else:
                xs.append(x)
                ys.append(y)

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    ax.plot(xs, ys, c=draw_args.get('color', 'r'))

    painter(ax, fig, draw_args)


def transform_formulae_painter(taxis_list=None, axis_type=normal, steps=2 ** 10,
                               func=None, draw_args=dict()):
    """x = f(t)
       y = f(t)"""
    xs, ys = [], []
    for taxis in taxis_list:
        for t in tqdm(np.linspace(*taxis, steps)):
            x, y = func(t)
            if axis_type == polar:
                xs.append(y * np.cos(x))
                ys.append(y * np.sin(x))
            else:
                xs.append(x)
                ys.append(y)

    fig = plt.figure(figsize=draw_args.get('figsize', None))
    ax = fig.add_subplot()

    ax.plot(xs, ys, c=draw_args.get('color', 'r'))

    painter(ax, fig, draw_args)


def fractal_painter(rule, angle, length, depth, start_angle=None, save_path=None, **kwargs):
    """几何分形作图"""
    import matplotlib.collections as collections

    path = rule['s']

    for i in range(depth):
        current_path = []
        for p in path:
            if p in rule:
                current_path.append(rule[p])
            else:
                current_path.append(p)
        path = "".join(current_path)

    p = (0.0, 0.0)
    start_angle = start_angle or 0
    lines = []
    stack = []
    for c in path:
        if c in "Ff":
            r = start_angle * pi / 180
            t = p[0] + length * cos(r), p[1] + length * sin(r)
            lines.append(((p[0], p[1]), (t[0], t[1])))
            p = t
        elif c == "+":
            start_angle += angle
        elif c == "-":
            start_angle -= angle
        elif c == "[":
            stack.append((p, start_angle))
        elif c == "]":
            p, start_angle = stack.pop(-1)

    fig, ax = plt.subplots()
    fig.set_facecolor("papayawhip")

    lc = collections.LineCollection(lines)
    ax.add_collection(lc, autolim=True)
    ax.axis("equal")
    ax.invert_yaxis()

    painter(ax, fig, draw_args={'save_path': save_path})


def fractal_painter_with_turtle(rule, angle, length, depth, t=None, start_point=None, start_angle=None, **kwargs):
    """调用turtle的分形作图"""
    import turtle

    path = rule['s']

    for i in range(depth):
        current_path = []
        for p in path:
            if p in rule:
                current_path.append(rule[p])
            else:
                current_path.append(p)
        path = "".join(current_path)

    if t is None:
        t = turtle.Turtle()

    t.hideturtle()
    t.speed('fastest')

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
        if p in 'fF':
            t.forward(length)
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


def chaos_fractal_painter(xs, ys, save_path=None):
    """混沌分形作图"""
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot()

    ax.scatter(xs, ys, s=1, marker=',')

    painter(ax, fig, draw_args={'save_path': save_path})


def attractor_painter(func, *args, dt=0.001, n_steps=100000, start_xyz=(0.1, 0.1, 0.1),
                      save_path=None, **kwargs):
    """吸引子作图"""
    xs = np.empty(n_steps + 1)
    ys = np.empty(n_steps + 1)
    zs = np.empty(n_steps + 1)

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

    ax.plot(xs, ys, zs, linewidth=1)

    painter(ax, fig, draw_args={'save_path': save_path})
