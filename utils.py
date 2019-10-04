import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

normal = 0
polar = 1


def draw(xs, ys, title, save_path):
    # plt.figure(figsize=(12, 12))
    plt.scatter(xs, ys, s=1, c='red', marker=',')
    plt.title(title)
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()


def paint2d_with_unpack_function_normal(xaxis, yaxis, steps, line_width, title, save_path, axis_type='normal'):
    def decorator(method):
        def paint(*args, **kwargs):
            func = method(*args, **kwargs)
            xs, ys = [], []
            for x in tqdm(np.linspace(*xaxis, steps)):
                for y in np.linspace(*yaxis, steps):
                    if abs(func(x, y)) < line_width:
                        xs.append(x)
                        ys.append(y)

            draw(xs, ys, title, save_path)

        return paint

    return decorator


def paint2d_with_unpack_function(xaxis=None, yaxis=None,
                                 axis_type=normal, taxis=None, raxis=None,
                                 steps=2 ** 13, line_width=2 ** -7,
                                 title='', save_path=None,
                                 func=None):
    def decorator(method):
        def paint(*args, **kwargs):
            def recursion(start_xx, start_yy, start_set, batch_steps, steps, line_width, ):
                step_width = (start_xx[1] - start_xx[0], start_yy[1] - start_yy[0])
                result = np.zeros((steps * batch_steps, steps * batch_steps), dtype=np.int8)

                for idn in tqdm(start_set):
                    idx, idy = idn[0], idn[1]

                    xx = np.linspace(start_xx[idx], start_xx[idx] + step_width[0], batch_steps)
                    yy = np.linspace(start_yy[idy], start_yy[idy] + step_width[1], batch_steps)

                    for i, x in enumerate(xx):
                        for j, y in enumerate(yy):
                            if abs(func(x, y)) < line_width:
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

            iterate = int(np.log2(steps)) - 6
            batch_steps = 2

            start_steps = steps // 2 ** (iterate + 1)
            start_line_width = line_width * 2 ** (iterate + 1)

            start_set = set()
            for i in range(start_steps):
                for j in range(start_steps):
                    start_set.add(tuple([i, j]))  # start border

            for _ in range(iterate):
                xx = np.linspace(*axis1, start_steps)
                yy = np.linspace(*axis2, start_steps)

                start_set = recursion(xx, yy, start_set, batch_steps, start_steps, start_line_width)

                start_steps *= 2
                start_line_width /= 2

            xs, ys = [], []
            xx = np.linspace(*axis1, start_steps)
            yy = np.linspace(*axis2, start_steps)

            for idn in start_set:
                x, y = xx[idn[0]], yy[idn[1]]
                if axis_type == polar:
                    xs.append(y * np.cos(x))
                    ys.append(y * np.sin(x))
                else:
                    xs.append(x)
                    ys.append(y)

            draw(xs, ys, title, save_path)

        return paint

    return decorator


def paint2d_with_equation_function(xaxis_list=None, axis_type=normal, taxis_list=None,
                                   steps=2 ** 10, func=None, title='', save_path=None):
    def decorator(method):
        def paint(*args, **kwargs):
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

            draw(xs, ys, title, save_path)

        return paint

    return decorator


def paint2d_with_transform_function(taxis_list=None, steps=2 ** 10,
                                    func=None, title='', save_path=None):
    def decorator(method):
        def paint(*args, **kwargs):
            xs, ys = [], []
            for taxis in taxis_list:
                for t in tqdm(np.linspace(*taxis, steps)):
                    x, y = func(t)
                    xs.append(x)
                    ys.append(y)

            draw(xs, ys, title, save_path)

        return paint

    return decorator


def paint3d(xaxis=(-1, 1), yaxis=(-1, 1), zaxis=(-1, 1), steps=1000, line_width=1e-3):
    """http://www.matrix67.com/blog/archives/223"""
    # a = np.linspace(*xaxis, steps)
    # b = np.linspace(*yaxis, steps)
    # zs = np.zeros((b.size, a.size)) - 2
    xs, ys, zs = [], [], []
    for z in tqdm(np.linspace(*zaxis, steps)):
        for i, x in enumerate(np.linspace(*xaxis, steps)):
            for j, y in enumerate(np.linspace(*yaxis, steps)):
                if abs((x ** 2 + 9 / 4 * y ** 2 + z ** 2 - 1) ** 3
                       - x ** 2 * z ** 3 - 9 / 80 * y ** 2 * z ** 3) < line_width:
                    xs.append(x)
                    ys.append(y)
                    zs.append(z)
                    # zs[j][i] = z

    # xs, ys = np.meshgrid(a, b)
    fig2, _ = plt.subplots()
    ax2 = Axes3D(fig2)
    ax2.scatter(xs, ys, zs, c='red', s=1, marker=',')
    # ax2.plot_surface(xs, ys, zs, cmap='rainbow')
    plt.show()
