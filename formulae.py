from utils import *


def heart1():
    """http://www.mathematische-basteleien.de/heart.htm"""

    implicit_formulae_painter(xaxis=(-1.5, 1.5), yaxis=(-1.5, 2),
                              func=lambda x, y: x ** 2 + (y - abs(x) ** (2 / 3)) ** 2 - 1, draw_args={
            'save_path': 'formulae/heart2D_1.png'
        })


# heart1()


def heart2():
    """http://www.mathematische-basteleien.de/heart.htm"""

    implicit_formulae_painter(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3, draw_args={
            'title': r'$\left ( x^2 + y^2 - 1 \right ) ^3 - x^2  y^3 = 0$',
            'save_path': 'formulae/heart2D_2.png'
        })


# heart2()


def heart3():
    """http://www.mathematische-basteleien.de/heart.htm"""

    implicit_formulae_painter(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              func=lambda x, y: x ** 2 + 2 * (3 / 5 * abs(x) ** (2 / 3) - y) ** 2 - 1, draw_args={
            'title': r'$x^2 + 2 \left ( \frac{3}{5} \sqrt[3]{x^2} - y \right ) ^ 2 - 1 = 0$',
            'save_path': 'formulae/heart2D_3.png'
        })


# heart3()


def heart4():
    """http://www.mathematische-basteleien.de/heart.htm"""
    implicit_formulae_painter(xaxis=(-2, 2), yaxis=(-2, 3), func=lambda x, y: x ** 2 + (y - abs(x) ** (1 / 2)) ** 2 - 3,
                              draw_args={
                                  'title': r'$x^2 + \left ( y - \sqrt {|x|} \right ) ^2 - 3 = 0$',
                                  'save_path': 'formulae/heart2D_4.png'
                              })


# heart4()


def heart5():
    """http://www.mathematische-basteleien.de/heart.htm"""
    transform_formulae_painter(taxis_list=((-1, 1),), steps=2 ** 10, func=lambda t: (sin(t) * cos(t) * np.log(abs(t)),
                                                                                     np.sqrt(abs(t)) * cos(t)),
                               draw_args={
                                   'title': r'$x = \sin (t) \cos (t) \ln (|t|)$' + '\n' +
                                            r'$y = \sqrt{|t|} \cos (t)$' + '\n' +
                                            r'$n-1 \leq t \leq 1$',
                                   'save_path': 'formulae/heart2D_5.png',
                               })


# heart5()


def heart6():
    """http://www.mathematische-basteleien.de/heart.htm"""
    implicit_formulae_painter(xaxis=(-4.5, 4.5), yaxis=(-4.5, 4.5),
                              func=lambda x, y: 17 * x ** 2 - 16 * abs(x) * y + 17 * y ** 2 + 150 / abs(
                                  5 * x + sin(5 * y)) - 225, draw_args={
            'title': r'$17x^2 - 16|x|y + 17y^2 + \frac{150}{|5x + \sin (5y)|} = 225$',
            'save_path': 'formulae/heart2D_6.png'
        })


# heart6()


def heart7():
    """http://www.mathematische-basteleien.de/heart.htm"""

    explicit_formulae_painter(axis_type=polar, taxis_list=((-pi, -pi / 2), (pi / 2, pi)), steps=2 ** 10,
                              func=lambda t: 5 * sin(t) ** 7 * exp(abs(2 * t)), draw_args={
            'title': r'$r = 5 \sin ^7 (t) e ^{|2t|}$',
            'save_path': 'formulae/heart2D_7.png',
        })


# heart7()


def heart8():
    """http://www.mathematische-basteleien.de/heart.htm"""

    explicit_formulae_painter(axis_type=polar, taxis_list=((-pi * 2, pi * 2),), steps=2 ** 10,
                              func=lambda t: 1 - sin(t), draw_args={
            'title': r'$r = 1 - \sin (t)$',
            'save_path': 'formulae/heart2D_8.png',
        })


# heart8()


def heart9():
    explicit_formulae_painter(xaxis_list=((-3.3 ** 0.5, 3.3 ** 0.5),), steps=2 ** 10,
                              func=lambda x: abs(x) ** (2 / 3) + 0.9 * (3.3 - x ** 2) ** 0.5 * sin(30 * pi * x),
                              draw_args={
                                  'title': r'$y = \sqrt[3]{x^2} + 0.9(3.3 - x^2)^{0.5} \cdot  \frac{\sin (b \pi  x)}{nb}=30$',
                                  'save_path': 'formulae/heart2D_9.png',
                              })


# heart9()


def equation1():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10),
                              func=lambda x, y: exp(sin(x) + cos(y)) - sin(exp(x + y)), draw_args={
            'title': r'$e^{\sin (x) + \cos (y)} = \sin (e^{x + y})$',
            'save_path': 'formulae/equation1.png',
            'figsize': (12, 12)
        })


# equation1()


def equation2():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10),
                              func=lambda x, y: sin(sin(x) + cos(y)) - cos(sin(x * y) - cos(x)), draw_args={
            'title': r'$\sin (\sin (x) + \cos (y)) = \cos (\sin (xy) + \cos (x))$',
            'save_path': 'formulae/equation2.png',
            'figsize': (12, 12)
        })


# equation2()


def equation3():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10), func=lambda x, y: sin(x ** 2 + y ** 2) - cos(x * y),
                              draw_args={
                                  'title': r'$\sin (x^2 + y^2) = \cos (xy)$',
                                  'save_path': 'formulae/equation3.png',
                                  'figsize': (12, 12)
                              })


# equation3()


def equation4():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10),
                              func=lambda x, y: abs(sin(x ** 2 + 2 * x * y)) - sin(x - 2 * y), draw_args={
            'title': r'$|\sin (x^2 + 2xy)| = \sin (x - 2y)$',
            'save_path': 'formulae/equation4.png',
            'figsize': (12, 12)
        })


# equation4()


def equation5():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10),
                              func=lambda x, y: abs(sin(x ** 2 - y ** 2)) - sin(x + y) - cos(x * y), draw_args={
            'title': r'$|\sin (x^2 - y^2)| = \sin (x + y) + \cos (xy)$',
            'save_path': 'formulae/equation5.png',
            'figsize': (12, 12)
        })


# equation5()


def equation6():
    """http://www.matrix67.com/blog/archives/4447"""

    implicit_formulae_painter(xaxis=(-10, 10), yaxis=(-10, 10),
                              func=lambda x, y: x / sin(x) + y / sin(y) - (x * y) / sin(x * y), draw_args={
            'title': r'$\frac{x}{\sin (x)} \pm \frac{y}{\sin (y)} = \pm \frac{xy}{\sin (xy)}$',
            'save_path': 'formulae/equation6.png',
            'figsize': (12, 12)
        })


# equation6()


def equation7():
    implicit_formulae_painter(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 2 - (x * y) ** 2, draw_args={
            'title': r'$(x^2 + y^2 - 1)^2 = (xy)^2$',
            'save_path': 'formulae/equation7.png',
            'figsize': (12, 12)
        })


# equation7()


def equation8():
    """https://www.zhihu.com/question/20603242"""

    explicit_formulae_painter(axis_type=polar, taxis_list=((-8 * pi, 8 * pi),), steps=2 ** 12,
                              func=lambda t: t + 3 * sin(4 * t) - 5 * cos(4 * t), draw_args={
            'title': r'$r = t + 3\sin (4t) - 5\cos (4t)$',
            'save_path': 'formulae/equation8.png',
            'figsize': (12, 12)
        })


# equation8()


def equation9():
    """https://www.zhihu.com/question/20603242"""

    implicit_formulae_painter(xaxis=(-5, 5), yaxis=(-5, 5), func=lambda x, y: sin(x ** 2 + y ** 2) - cos(x - y),
                              draw_args={
                                  'title': r'$\sin (x^2 + y^2) = \cos (x - y)$',
                                  'save_path': 'formulae/equation9.png',
                                  'figsize': (12, 12)
                              })


# equation9()


def equation10():
    """https://www.zhihu.com/question/20603242"""

    implicit_formulae_painter(xaxis=(-4 * pi, 4 * pi), yaxis=(-4 * pi, 4 * pi),
                              func=lambda x, y: sin(x) ** sin(y) + sin(y) ** sin(x) - sin(
                                  x ** 2 + y ** 2), draw_args={
            'title': r'$\sin (x^2 + y^2) = \sin (x)^{\sin (y)} + \sin (y)^{\sin (x)}$',
            'save_path': 'formulae/equation10.png',
            'figsize': (12, 12),
        })


# equation10()


def equation11():
    """http://www.matrix67.com/blog/archives/6947"""

    transform_formulae_painter(taxis_list=((-pi, pi),), steps=2 ** 10, func=lambda t: (sin(13 * t),
                                                                                       sin(18 * t)), draw_args={
        'title': r'$x = \sin (13t)$' + '\n' +
                 r'$y = \sin (18t)$' + '\n' +
                 r'$-1 \leq t \leq 1$',
        'save_path': 'formulae/equation11.png',
        'figsize': (12, 12)
    })


# equation11()


def nb():
    """https://www.zhihu.com/question/20603242"""

    implicit_formulae_painter(xaxis=(-3, 4), yaxis=(-2, 2),
                              func=lambda x, y: (1 + 2 * np.sqrt(-(abs(y) - 1) ** 2 + 1) - x) * (
                                      x ** 3 + x ** 2 - 2 * x) * (y + 2 * x + 2), draw_args={
            'title': r'$(1 + 2\sqrt{-(|y|-1)^2 + 1} - x)(x^3 + x^2 - 2x)(y + 2x + 2) = 0$',
            'save_path': 'formulae/nb.png',
            'figsize': (12, 12),
            'xlim': (-4, 5),
            'ylim': (-4, 4)
        })


# nb()


def butterfly():
    """https://www.zhihu.com/question/20603242"""

    explicit_formulae_painter(axis_type=polar, taxis_list=((-12 * pi, 12 * pi),), steps=2 ** 12,
                              func=lambda t: 2.7 ** sin(t) - 2 * cos(4 * t) + sin(
                                  (2 * t - pi) / 24) ** 5, draw_args={
            'title': r'$r = 2.7^{\sin (t)} - 2\cos (4t) + \sin ^ 5 (\frac{2t - \pi}{24})$' + '\n' +
                     r'$-12\pi < t < 12\pi$',
            'save_path': 'formulae/butterfly.png',
            'figsize': (12, 12),
            'color': 'b'
        })


# butterfly()


def yinyang():
    """http://www.matrix67.com/blog/archives/4447"""
    implicit_formulae_painter(axis_type=polar, taxis=(0, 2 * pi), raxis=(0, 4),
                              func=lambda t, r: (cos(t - r) - sin(t)) * (
                                      r ** 4 - 2 * r ** 2 * cos(2 * t + 2.4) + 0.9) + (0.62 * r) ** 100, draw_args={
            'title': r'$(\cos (t - r) - \sin (t))(r^4 - 2r^{2\cos (2t + 2.4)} + 0.9) + (0.62r)^{1000} = 0$',
            'save_path': 'formulae/yinyang.png',
            'color': 'black',
            'figsize': (12, 12),
            'xlim': (-2, 2),
            'ylim': (-2, 2)
        })


# yinyang()


def bird():
    """https://www.zhihu.com/question/20603242"""

    implicit_formulae_painter(xaxis=(-5, 5), yaxis=(-5, 5),
                              func=lambda x, y: (((x ** 2 + y ** 2) * ((x - 0.05) ** 2 / 4 + (y + 3) ** 2 / 16) * (
                                      (x + 2) ** 2 / 49 + (y - 3) ** 2 / 25) - 1.2) * (
                                                         (x + 3) ** 2 + 25 * (y - 2.8) ** 2 - 1) - 1) * (
                                                        (x + 2) ** 2 + (y - 2.8) ** 2 - 0.04), draw_args={
            'title': r'$(1 + 2\sqrt{-(|y|-1)^2 + 1} - x)(x^3 + x^2 - 2x)(y + 2x + 2) = 0$',
            'save_path': 'formulae/bird.png',
            'figsize': (12, 12),
            'xlim': (-5, 5),
            'ylim': (-5, 5)
        })


# bird()


def maurer_rose(n, d):
    transform_formulae_painter(taxis_list=((0, 360),), axis_type=polar, steps=360,
                               func=lambda t: (d * 0.0174533 * t, np.sin(n * d * 0.0174533 * t)), draw_args={
            'title': r'$r = \sin (n * d * t)$' + '\n' +
                     f'$n = {n},d = {d}$',
            'figsize': (12, 12),
            'save_path': f'formulae/maurer_rose_{n}_{d}.png',
        })


# nd_list = [[2, 71], [2, 91], [3, 31], [3, 61], [4, 41], [4, 91],
#            [5, 31], [6, 31], [8, 71]]
#
# for nd in nd_list:
#     maurer_rose(*nd)


def spiral():
    k = 0
    colors = ['seagreen', 'darkseagreen', 'darkgreen', 'yellowgreen']
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot()
    x, y = 1, 1
    for i in range(400):
        l = 2 * i
        y_ = y + l * np.sin(k)
        x_ = x + l * np.cos(k)
        ax.plot([x, x_], [y, y_], c=colors[i % 4])

        k += np.pi * 91 / 180
        x, y = x_, y_

    painter(ax, fig, draw_args={'save_path': 'formulae/spiral.png'})


# spiral()
