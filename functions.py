from utils import *


@paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 2),
                              steps=2 ** 13, line_width=2 ** -7,
                              title='x^2 + (y - |x|^(2/3))^2) - 1 = 0',
                              func=lambda x, y: x ** 2 + (y - abs(x) ** (2 / 3)) ** 2 - 1,
                              save_path='img/heart2D_1.png')
def heart1():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              steps=2 ** 13, line_width=2 ** -7,
                              title='(x^2 + y^2 - 1)^3 - x^2 * y^3 = 0',
                              func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3,
                              save_path='img/heart2D_2.png')
def heart2():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              steps=2 ** 13, line_width=2 ** -7,
                              title='x^2 + 2(3/5|x|^(2/3) - y)^2 - 1 = 0',
                              func=lambda x, y: x ** 2 + 2 * (3 / 5 * abs(x) ** (2 / 3) - y) ** 2 - 1,
                              save_path='img/heart2D_3.png')
def heart3():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_unpack_function(xaxis=(-2, 2), yaxis=(-2, 3),
                              steps=2 ** 13, line_width=2 ** -7,
                              title='x^2 + (y - sqrt(|x|))^2 - 3 = 0',
                              func=lambda x, y: x ** 2 + (y - abs(x) ** (1 / 2)) ** 2 - 3,
                              save_path='img/heart2D_4.png')
def heart4():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_transform_function(taxis_list=((-1, 1),), steps=2 ** 13,
                                 title='x = sin(t)cos(t)ln|t|\ny = sqrt(|t|)cos(t)\n-1 <= t <= 1',
                                 func=lambda t: (np.sin(t) * np.cos(t) * np.log(abs(t)), np.sqrt(abs(t)) * np.cos(t)),
                                 save_path='img/heart2D_5.png')
def heart5():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_unpack_function(xaxis=(-4.5, 4.5), yaxis=(-4.5, 4.5),
                              steps=2 ** 13, line_width=2 ** -2,
                              title='17x^2 - 16|x|y + 17y^2 = 225',
                              func=lambda x, y: 17 * x ** 2 - 16 * abs(x) * y + 17 * y ** 2 - 225,
                              save_path='img/heart2D_6.png')
def heart6():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_equation_function(axis_type=polar,
                                taxis_list=((-np.pi, -np.pi / 2), (np.pi / 2, np.pi)),
                                steps=2 ** 13,
                                title='r = 5 * sin(t)^7 * exp(|2t|)',
                                func=lambda t: 5 * np.sin(t) ** 7 * np.exp(abs(2 * t)),
                                save_path='img/heart2D_7.png')
def heart7():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_equation_function(axis_type=polar,
                                taxis_list=((-np.pi * 2, np.pi * 2),),
                                steps=2 ** 13,
                                title='r = 1 - sin(t)',
                                func=lambda t: 1 - np.sin(t),
                                save_path='img/heart2D_8.png')
def heart8():
    """http://www.mathematische-basteleien.de/heart.htm"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='exp(sin(x) + cos(y)) = sin(exp(x + y))',
                              func=lambda x, y: np.exp(np.sin(x) + np.cos(y)) - np.sin(np.exp(x + y)),
                              save_path='img/equation1.png')
def equation1():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='sin(sin(x) + cos(y)) = cos(sin(xy) + cos(x))',
                              func=lambda x, y: np.sin(np.sin(x) + np.cos(y)) - np.cos(np.sin(x * y) - np.cos(x)),
                              save_path='img/equation2.png')
def equation2():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='sin(x^2 + y^2) = cos(xy)',
                              func=lambda x, y: np.sin(x ** 2 + y ** 2) - np.cos(x * y),
                              save_path='img/equation3.png')
def equation3():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='|sin(x^2 + 2xy)| = sin(x - 2y)',
                              func=lambda x, y: abs(np.sin(x ** 2 + 2 * x * y)) - np.sin(x - 2 * y),
                              save_path='img/equation4.png')
def equation4():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='|sin(x^2 - y^2)| = sin(x + y) + cos(xy)',
                              func=lambda x, y: abs(np.sin(x ** 2 - y ** 2)) - np.sin(x + y) - np.cos(x * y),
                              save_path='img/equation5.png')
def equation5():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-10, 10), yaxis=(-10, 10),
                              steps=2 ** 13, line_width=2 ** -5,
                              title='x/sin(x) + y/sin(y) = xy/sin(xy)',
                              func=lambda x, y: x / np.sin(x) - y / np.sin(y) - (x * y) / np.sin(x * y),
                              save_path='img/equation6.png')
def equation6():
    """http://www.matrix67.com/blog/archives/4447"""


@paint2d_with_unpack_function(xaxis=(-1.5, 1.5), yaxis=(-1.5, 1.5),
                              steps=2 ** 13, line_width=2 ** -7,
                              title='(x^2 + y^2 - 1)^2 = (xy)^2',
                              func=lambda x, y: (x ** 2 + y ** 2 - 1) ** 2 - (x * y) ** 2,
                              save_path='img/equation7.png')
def equation7():
    pass


if __name__ == '__main__':
    heart5()
