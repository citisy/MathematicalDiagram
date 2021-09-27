from utils import *


def dragon_curve(length=2, depth=14):
    """http://blog.sciencenet.cn/blog-677221-601957.html

    main process:
    2nd recursion: r r l
    3rd recursion: rrl r rll
    4th recursion: rrlrrll r rrllrll
    ......

    right part and left part, it's symmetric"""

    angle = 90
    fractal_painter_with_plt({'s': 'Fr', 'r': 'r+lF+', 'l': '-Fr-l'},
                             angle, length, depth,
                             draw_args={
                                 # 'save_path': 'fractal/dragon_curve_depth=%d.png' % depth,
                             })


dragon_curve(depth=14)


def koch_curve(length=2, depth=5):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 60
    start_point = (-length * 3 ** depth / 2, length * 3 ** depth / 2 / 3 ** 0.5)

    fractal_painter_with_plt({'s': 'F++F++F', 'F': 'F-F++F-F'},
                             angle, length, depth, start_point=start_point,
                             draw_args={
                                 # 'save_path': 'fractal/koch_curve_depth=%d.png' % depth
                             })


# koch_curve(depth=5)


def pythagoras_tree(p0=(-50, -200), p1=(50, -200), depth=10, save_path=None):
    """p0, p1: left bottom point and right bottom point of square"""

    def recursion(x0, y0, x1, y1, depth=0):
        if depth > 0:
            dx, dy = x1 - x0, y1 - y0
            x2, y2 = x1 - dy, y1 + dx
            x3, y3 = x0 - dy, y0 + dx
            x4, y4 = x3 + (dx - dy) / 2, y3 + (dx + dy) / 2

            ax.fill([x0, x1, x2, x3], [y0, y1, y2, y3], c='steelblue')

            recursion(x3, y3, x4, y4, depth - 1)
            recursion(x4, y4, x2, y2, depth - 1)

    fig, ax = plt.subplots()
    recursion(*p0, *p1, depth=depth)

    fig.set_facecolor("papayawhip")
    ax.axis("equal")
    ax.set_axis_off()

    # save_path='fractal/pythagoras_tree_depth=%d.png' % depth

    if save_path is not None:
        fig.savefig(save_path, facecolor=fig.get_facecolor())

    plt.show()


# pythagoras_tree(depth=10)


def sierpinski_triangle(p0=(-250, -200), p1=(250, -200), depth=6, save_path=None):
    """p0, p1: left bottom point and right bottom point of triangle"""

    def recursion(p0, p1, p2, depth=0):
        if depth == 0:
            ax.fill([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], c='steelblue')
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

    fig, ax = plt.subplots()
    recursion(p0, p1, p2, depth=depth)

    fig.set_facecolor("papayawhip")
    ax.axis("equal")
    ax.set_axis_off()

    # save_path = 'fractal/sierpinski_triangle_depth=%d.png' % depth

    if save_path is not None:
        fig.savefig(save_path, facecolor=fig.get_facecolor())

    plt.show()


# sierpinski_triangle(depth=6)


def sierpinski_triangle2(length=0.5, depth=5):
    angle = 60
    start_point = (-length * 4 ** depth / 2, -length * 4 ** depth / 2 / 3 ** 0.5)
    fractal_painter_with_plt({'s': 'rF', 'r': 'rF-lF-rF+lF+rF+lF+rF-lF-r', 'l': 'lF+rF+lF-rF-lF-rF-lF+rF+l'}, angle,
                             length, depth, start_point=start_point,
                             draw_args={
                                 # 'save_path': 'fractal/sierpinski_triangle2_depth=%d.png' % depth
                             })


# sierpinski_triangle2(depth=5)


def sierpinski_triangle3(length=2, depth=7):
    angle = 60
    fractal_painter_with_plt({'s': 'rF', 'r': 'lF-rF-l', 'l': 'rF+lF+r'},
                             angle, length, depth,
                             draw_args={
                                 # 'save_path': 'fractal/sierpinski_triangle3_depth=%d.png' % depth
                             })


# sierpinski_triangle3(depth=7)


def sierpinski(length=5, depth=10):
    angle = 45
    fractal_painter_with_plt({'s': 'l--F--l--F', 'l': '+r-F-r+', 'r': '-l+F+l-'},
                             angle, length, depth,
                             draw_args={
                                 # 'save_path': 'fractal/sierpinski_depth=%d.png' % depth
                             })


# sierpinski(depth=10)


def lvey_c(length=2, depth=14):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 45
    start_point = (-length * 2 ** (depth / 2 - 1), length * 2 ** (depth / 2 - 2))
    fractal_painter_with_plt({'s': 'F', 'F': '+F--F+'},
                             angle, length, depth, start_point=start_point,
                             draw_args={
                                 # 'save_path': 'fractal/lvey_c_depth=%d.png' % depth
                             })


# lvey_c(depth=14)


def hilbert(length=10, depth=5):
    angle = 90
    fractal_painter_with_plt({'s': 'r', 'r': '-lF+rFr+Fl-', 'l': '+rF-lFl-Fr+'},
                             angle, length, depth,
                             draw_args={
                                 # 'save_path': 'fractal/hilbert_depth=%d.png' % depth
                             })


# hilbert(depth=5)


def leaf(length=2, depth=6):
    angle = 25
    fractal_painter_with_plt({'s': 'x', 'x': 'F-[[x]+x]+F[+Fx]-x', 'F': 'FF'},
                             angle, length, depth, start_angle=-45,
                             draw_args={
                                 # 'save_path': 'fractal/leaf_depth=%d.png' % depth
                             })


# leaf(depth=6)
