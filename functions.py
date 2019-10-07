from utils import *


def heart1():
    """http://www.mathematische-basteleien.de/heart.htm"""

    paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 2),
                                 steps=2 ** 13, line_width=2 ** -7,
                                 func=lambda x, y: x ** 2 + (y - abs(x) ** (2 / 3)) ** 2 - 1,
                                 draw_args={'title': 'x^2 + (y - |x|^(2/3))^2) - 1 = 0',
                                            'save_path': 'img/heart2D_1.png'}
                                 )


def heart2():
    """http://www.mathematische-basteleien.de/heart.htm"""

    paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                                 steps=2 ** 13, line_width=2 ** -7,
                                 func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3,
                                 draw_args={'title': '(x^2 + y^2 - 1)^3 - x^2 * y^3 = 0',
                                            'save_path': 'img/heart2D_2.png'}
                                 )


def heart3():
    """http://www.mathematische-basteleien.de/heart.htm"""

    paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                                 steps=2 ** 13, line_width=2 ** -7,
                                 func=lambda x, y: x ** 2 + 2 * (3 / 5 * abs(x) ** (2 / 3) - y) ** 2 - 1,
                                 draw_args={'title': 'x^2 + 2(3/5|x|^(2/3) - y)^2 - 1 = 0',
                                            'save_path': 'img/heart2D_3.png'}
                                 )


def heart4():
    """http://www.mathematische-basteleien.de/heart.htm"""
    paint2d_with_unpack_function(xaxis=(-2, 2), yaxis=(-2, 3),
                                 steps=2 ** 13, line_width=2 ** -7,
                                 func=lambda x, y: x ** 2 + (y - abs(x) ** (1 / 2)) ** 2 - 3,
                                 draw_args={'title': 'x^2 + (y - sqrt(|x|))^2 - 3 = 0',
                                            'save_path': 'img/heart2D_4.png'}
                                 )


def heart5():
    """http://www.mathematische-basteleien.de/heart.htm"""
    paint2d_with_transform_function(taxis_list=((-1, 1),), steps=2 ** 10,
                                    func=lambda t: (np.sin(t) * np.cos(t) * np.log(abs(t)),
                                                    np.sqrt(abs(t)) * np.cos(t)),
                                    draw_args={'title': 'x = sin(t)cos(t)ln|t|\ny = sqrt(|t|)cos(t)\n-1 <= t <= 1',
                                               'save_path': 'img/heart2D_5.png',
                                               'draw_type': plot}
                                    )


def heart6():
    """http://www.mathematische-basteleien.de/heart.htm"""
    paint2d_with_unpack_function(xaxis=(-4.5, 4.5), yaxis=(-4.5, 4.5),
                                 steps=2 ** 15, line_width=2 ** 0,
                                 func=lambda x, y: 17 * x ** 2 - 16 * abs(x) * y + 17 * y ** 2 + 150 / abs(
                                     5 * x + np.sin(5 * y)) - 225,
                                 draw_args={'title': '17x^2 - 16|x|y + 17y^2 + 150/|5x + sin(5y)| = 225',
                                            'save_path': 'img/heart2D_6.png'}
                                 )


def heart7():
    """http://www.mathematische-basteleien.de/heart.htm"""

    paint2d_with_equation_function(axis_type=polar,
                                   taxis_list=((-np.pi, -np.pi / 2), (np.pi / 2, np.pi)),
                                   steps=2 ** 10,
                                   func=lambda t: 5 * np.sin(t) ** 7 * np.exp(abs(2 * t)),
                                   draw_args={'title': 'r = 5 * sin(t)^7 * exp(|2t|)',
                                              'save_path': 'img/heart2D_7.png',
                                              'draw_type': plot}
                                   )


def heart8():
    """http://www.mathematische-basteleien.de/heart.htm"""

    paint2d_with_equation_function(axis_type=polar,
                                   taxis_list=((-np.pi * 2, np.pi * 2),),
                                   steps=2 ** 10,
                                   func=lambda t: 1 - np.sin(t),
                                   draw_args={'title': 'r = 1 - sin(t)',
                                              'save_path': 'img/heart2D_8.png',
                                              'draw_type': plot}
                                   )


def equation1():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -5,
                                 func=lambda x, y: np.exp(np.sin(x) + np.cos(y)) - np.sin(np.exp(x + y)),
                                 draw_args={'title': 'exp(sin(x) + cos(y)) = sin(exp(x + y))',
                                            'save_path': 'img/equation1.png'}
                                 )


def equation2():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -5,
                                 func=lambda x, y: np.sin(np.sin(x) + np.cos(y)) - np.cos(np.sin(x * y) - np.cos(x)),
                                 draw_args={'title': 'sin(sin(x) + cos(y)) = cos(sin(xy) + cos(x))',
                                            'save_path': 'img/equation2.png'}
                                 )


def equation3():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -5,
                                 func=lambda x, y: np.sin(x ** 2 + y ** 2) - np.cos(x * y),
                                 draw_args={'title': 'sin(x^2 + y^2) = cos(xy)',
                                            'save_path': 'img/equation3.png'}
                                 )


def equation4():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -5,
                                 func=lambda x, y: abs(np.sin(x ** 2 + 2 * x * y)) - np.sin(x - 2 * y),
                                 draw_args={'title': '|sin(x^2 + 2xy)| = sin(x - 2y)',
                                            'save_path': 'img/equation4.png'}
                                 )


def equation5():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -5,
                                 func=lambda x, y: abs(np.sin(x ** 2 - y ** 2)) - np.sin(x + y) - np.cos(x * y),
                                 draw_args={'title': '|sin(x^2 - y^2)| = sin(x + y) + cos(xy)',
                                            'save_path': 'img/equation5.png'}
                                 )


def equation6():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                                 steps=2 ** 13, line_width=2 ** -2,
                                 # func=lambda x, y: [
                                 #                    x / np.sin(x) + y / np.sin(y) - (x * y) / np.sin(x * y),
                                 #                    x / np.sin(x) - y / np.sin(y) + (x * y) / np.sin(x * y),
                                 #                    x / np.sin(x) + y / np.sin(y) + (x * y) / np.sin(x * y)],
                                 func=lambda x, y: [
                                     (x / np.sin(x)) ** 2 - (y / np.sin(y) - (x * y) / np.sin(x * y)) ** 2,
                                     (x / np.sin(x)) ** 2 - (y / np.sin(y) + (x * y) / np.sin(x * y)) ** 2,
                                 ],
                                 draw_args={'title': 'x/sin(x) +- y/sin(y) = +-xy/sin(xy)',
                                            'save_path': 'img/equation6.png'}
                                 )


def equation7():
    paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                                 steps=2 ** 13, line_width=2 ** -7,
                                 func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 2 - (x * y) ** 2,
                                 draw_args={'title': '(x^2 + y^2 - 1)^2 = (xy)^2',
                                            'save_path': 'img/equation7.png'}
                                 )


def equation8():
    """https://www.zhihu.com/question/20603242"""

    paint2d_with_equation_function(axis_type=polar, taxis_list=((-8 * np.pi, 8 * np.pi),),
                                   steps=2 ** 12,
                                   func=lambda t: t + 3 * np.sin(4 * t) - 5 * np.cos(4 * t),
                                   draw_args={'title': 'r = t + 3sin(4t) - 5cos(4t)',
                                              'save_path': 'img/equation8.png',
                                              'draw_type': plot,
                                              'figsize': (12, 12)}
                                   )


def equation9():
    """https://www.zhihu.com/question/20603242"""

    paint2d_with_unpack_function(xaxis=(-5, 5), yaxis=(-5, 5),
                                 steps=2 ** 13, line_width=2 ** -6,
                                 func=lambda x, y: np.sin(x ** 2 + y ** 2) - np.cos(x - y),
                                 draw_args={'title': 'sin(x^2 + y^2) = cos(x - y)',
                                            'save_path': 'img/equation9.png',
                                            'figsize': (12, 12)}
                                 )


def equation10():
    """https://www.zhihu.com/question/20603242"""

    paint2d_with_unpack_function(xaxis=(-4 * np.pi, 4 * np.pi), yaxis=(-4 * np.pi, 4 * np.pi),
                                 steps=2 ** 12, line_width=2 ** -3,
                                 func=lambda x, y: np.sin(x) ** np.sin(y) + np.sin(y) ** np.sin(x) - np.sin(
                                     x ** 2 + y ** 2),
                                 draw_args={'title': 'sin(x^2 + y^2) = sin(x)^sin(y) + sin(y)^sin(x)',
                                            'save_path': 'img/equation10.png',
                                            'figsize': (12, 12),
                                            }
                                 )


def nb():
    """https://www.zhihu.com/question/20603242"""

    paint2d_with_unpack_function(xaxis=(-3, 4), yaxis=(-2, 2),
                                 steps=2 ** 13, line_width=2 ** -2,
                                 func=lambda x, y: (1 + 2 * np.sqrt(-(abs(y) - 1) ** 2 + 1) - x) * (
                                         x ** 3 + x ** 2 - 2 * x) * (y + 2 * x + 2),
                                 draw_args={'title': '(1 + 2sqrt(-(|y|-1)^2 + 1) - x)(x^3 + x^2 - 2x)(y + 2x + 2) = 0',
                                            'save_path': 'img/nb.png',
                                            'figsize': (12, 12),
                                            'xlim': (-4, 5),
                                            'ylim': (-4, 4)}
                                 )


def butterfly():
    """https://www.zhihu.com/question/20603242"""

    paint2d_with_equation_function(axis_type=polar, taxis_list=((-12 * np.pi, 12 * np.pi),),
                                   steps=2 ** 12,
                                   func=lambda t: 2.7 ** np.sin(t) - 2 * np.cos(4 * t) + np.sin(
                                       (2 * t - np.pi) / 24) ** 5,
                                   draw_args={
                                       'title': 'r = 2.7^sin(t) - 2cos(4t) + sin((2t - pi)/24)^5\n-12pi < t < 12pi',
                                       'save_path': 'img/butterfly.png',
                                       'draw_type': plot,
                                       'figsize': (12, 12),
                                       'color': 'b'}
                                   )


def yinyang():
    """http://www.matrix67.com/blog/archives/4447"""
    paint2d_with_unpack_function(axis_type=polar, taxis=(0, 2 * np.pi), raxis=(0, 4),
                                 steps=2 ** 12, line_width=2 ** -7,
                                 func=lambda t, r: (np.cos(t - r) - np.sin(t)) * (
                                         r ** 4 - 2 * r ** 2 * np.cos(2 * t + 2.4) + 0.9) + (0.62 * r) ** 100,
                                 draw_args={
                                     'title': '(cos(t - r) - sin(t))(r^4 - 2r^2cos(2t + 2.4) + 0.9) + (0.62r)^1000 = 0',
                                     'save_path': 'img/yinyang.png',
                                     'color': 'black',
                                     'figsize': (12, 12),
                                     'xlim': (-2, 2),
                                     'ylim': (-2, 2)}
                                 )


def bird():
    """https://www.zhihu.com/question/20603242"""

    # todo: 精度不够，只有头部
    paint2d_with_unpack_function(xaxis=(-5, 5), yaxis=(-5, 5),
                                 steps=2 ** 13, line_width=2 ** -2,
                                 func=lambda x, y: (((x ** 2 + y ** 2) * ((x - 0.05) ** 2 / 4 + (y + 3) ** 2 / 16) * (
                                         (x + 2) ** 2 / 49 + (y - 3) ** 2 / 25) - 1.2) * (
                                                            (x + 3) ** 2 + 25 * (y - 2.8) ** 2 - 1) - 1) * (
                                                           (x + 2) ** 2 + (y - 2.8) ** 2 - 0.04),
                                 draw_args={'title': '(1 + 2sqrt(-(|y|-1)^2 + 1) - x)(x^3 + x^2 - 2x)(y + 2x + 2) = 0',
                                            'save_path': 'img/bird.png',
                                            'figsize': (12, 12),
                                            'xlim': (-5, 5),
                                            'ylim': (-5, 5)}
                                 )


if __name__ == '__main__':
    yinyang()
