from utils import *


def dragon_curve(length=2, depth=14, save_path=None):
    """http://blog.sciencenet.cn/blog-677221-601957.html

    main process:
    2nd recursion: r r l
    3rd recursion: rrl r rll
    4th recursion: rrlrrll r rrllrll
    ......

    right part and left part, it's symmetric"""

    angle = 90
    fractal_painter({'s': 'fr', 'r': 'r+lf+', 'l': '-fr-l'}, angle, length, depth, save_path=save_path)


def koch_curve(length=2, depth=5, save_path=None):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 60
    start_point = (-length * 3 ** depth / 2, length * 3 ** depth / 2 / 3 ** 0.5)

    fractal_painter({'s': 'f++f++f', 'f': 'f-f++f-f'}, angle, length, depth, save_path=save_path,
                    start_point=start_point)


# koch_curve()


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

    if save_path is not None:
        fig.savefig(save_path, facecolor=fig.get_facecolor())

    plt.show()


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

    if save_path is not None:
        fig.savefig(save_path, facecolor=fig.get_facecolor())

    plt.show()


def sierpinski_triangle2(length=0.5, depth=5, save_path=None):
    angle = 60
    start_point = (-length * 4 ** depth / 2, -length * 4 ** depth / 2 / 3 ** 0.5)
    fractal_painter({'s': 'F', 'F': 'F-f-F+f+F+f+F-f-F', 'f': 'f+F+f-F-f-F-f+F+f'}, angle, length, depth,
                    save_path=save_path, start_point=start_point)


def sierpinski_triangle3(length=2, depth=7, save_path=None):
    angle = 60
    fractal_painter({'s': 'f', 'f': 'F-f-F', 'F': 'f+F+f'}, angle, length, depth, save_path=save_path)


def sierpinski(length=5, depth=10, save_path=None):
    angle = 45
    fractal_painter({'s': 'l--f--l--f', 'l': '+r-f-r+', 'r': '-l+f+l-'}, angle, length, depth, save_path=save_path)


def lvey_c(length=2, depth=14, save_path=None):
    """http://www.matrix67.com/blog/archives/6231#more-6231"""

    angle = 45
    start_point = (-length * 2 ** (depth / 2 - 1), length * 2 ** (depth / 2 - 2))
    fractal_painter({'s': 'f', 'f': '+f--f+'}, angle, length, depth, save_path=save_path, start_point=start_point)


def hilbert(length=10, depth=5, save_path=None):
    angle = 90
    fractal_painter({'s': 'r', 'r': '-lf+rfr+fl-', 'l': '+rf-lfl-fr+'}, angle, length, depth, save_path=save_path)


def leaf(length=2, depth=6, save_path=None):
    angle = 25
    fractal_painter({'s': 'x', 'x': 'f-[[x]+x]+f[+fx]-x', 'f': 'ff'}, angle, length, depth, start_angle=-45,
                    save_path=save_path)


if __name__ == '__main__':
    depth = 6
    sierpinski_triangle(depth=depth, save_path='fractal/sierpinski_triangle%d.png' % depth)
