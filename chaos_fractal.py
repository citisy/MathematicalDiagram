from PIL import Image
from utils import *

mandelbrot_set = 0
julia_set = 1


def colorful_fractal_set(xaxis, yaxis, size, r=2, maxiter=100,
                         fractal_type=mandelbrot_set, c=complex(0, 0), save_path=None):
    def color(z, i):
        """https://www.reddit.com/r/math/comments/2abwyt/smooth_colour_mandelbrot/"""
        v = np.log2(i + r - np.log2(np.log2(abs(z)))) / 4
        if v < 1.0:  # background color
            return v ** 4, v ** 2.5, v ** 1
        else:
            v = max(0, 2 - v)
            return v ** 0.9, v ** 0.9, v ** 0.9

    def mandelbrot(c):
        z = c
        for i in range(maxiter):
            if abs(z) > r:
                return np.uint8(np.dstack(color(z, i)) * 255)
            z = z ** 2 + c
        return 0, 0, 0

    def julia(z):
        for i in range(maxiter):
            if abs(z) > r:
                return np.uint8(np.dstack(color(z, i)) * 255)
            z = z ** 2 + c
        return 0, 0, 0

    width, height = size

    r1 = np.linspace(*xaxis, width)
    r2 = np.linspace(*yaxis, height)
    img_array = np.zeros((height, width, 3), dtype=np.uint8)

    for idx1, x in tqdm(enumerate(r1)):
        for idx2, y in enumerate(r2):
            if fractal_type == mandelbrot_set:
                img_array[idx2, idx1] = mandelbrot(complex(x, y))
            else:
                img_array[idx2, idx1] = julia(complex(x, y))

    img = Image.fromarray(img_array)

    if save_path:
        img.save(save_path)

    # img.show()

    return img_array


# fractal_set((-2.0, 0.5), (-1.25, 1.25), (1000, 1000), save_path='fractal/mandelbrot_set.png')
# fractal_set((.275, .28), (.006, .01), (1000, 1000), save_path='fractal/elephant_valley.png')
# fractal_set((-.09, -.086), (.654, .657), (1000, 1000), save_path='fractal/triple_spiral_valley.png')
# fractal_set((-.75, -.747), (.099, .102), (1000, 1000), save_path='fractal/seahorse_valley.png')

# from moviepy.editor import ImageSequenceClip
# n = 60
# seq = []
# for i in range(n):
#     theta = 2 * np.pi / n * i
#     c = -(0.835 - 0.1 * np.cos(theta)) - (0.2321 + 0.1 * np.sin(theta)) * 1j
#     img = fractal_set((-1.5, 1.5), (-1.5, 1.5), (500, 500), c=c,
#                       fractal_type=julia_set)
#     seq.append(img)
# clip = ImageSequenceClip(seq, fps=10)
# clip.write_gif('fractal/julia_set.gif', fps=10)


def mandelbrot(save_path=None):
    xs, ys = [], []
    for x in tqdm(np.linspace(-2.0, 0.5, 1000)):
        for y in np.linspace(-1.25, 1.25, 1000):
            z = c = complex(x, y)
            for i in range(100):
                if abs(z) > 2:
                    break
                z = z ** 2 + c
            else:
                xs.append(x)
                ys.append(y)

    chaos_fractal_painter(xs, ys, save_path)


# mandelbrot(save_path='fractal/mandelbrot.png')


def julia(save_path=None):
    c = complex(-(0.835 - 0.1 * np.cos(np.pi)), -(0.2321 + 0.1 * np.sin(np.pi)))
    xs, ys = [], []
    for x in tqdm(np.linspace(-1.5, 1.5, 1000)):
        for y in np.linspace(-1.5, 1.5, 1000):
            z = complex(x, y)
            for i in range(100):
                if abs(z) > 2:
                    break
                z = z ** 2 + c
            else:
                xs.append(x)
                ys.append(y)

    chaos_fractal_painter(xs, ys, save_path)


# julia(save_path='fractal/julia.png')


def newton_iterate(save_path=None):
    """https://www.cnblogs.com/WhyEngine/p/4069145.html
    https://www.douban.com/note/230496472/"""

    xs, ys = [], []
    eps = 1e-6
    for x0 in tqdm(np.linspace(-1, 1, 500)):
        for y0 in np.linspace(-1, 1, 500):
            z = complex(x0, y0)
            for t in range(1000):
                if z == 0:
                    y = 0
                    break
                y = z - (z ** 3 - 1) / (3 * z ** 2)
                if abs(y - z) < eps:
                    if abs(y - 1) < eps:
                        xs.append(x0)
                        ys.append(y0)
                    break
                z = y

    chaos_fractal_painter(xs, ys, save_path)


# newton_iterate(save_path='fractal/newton_iterate.png')


def logistic(save_path=None):
    """http://wiki.swarma.net/index.php/Logistic%E6%98%A0%E5%B0%84"""
    xs, ys = [], []
    for x in tqdm(np.linspace(0.9, 4, 1000)):
        for y in np.linspace(0.1, 0.9, 100):
            for t in range(1000):
                y = x * y * (1 - y)
            xs.append(x)
            ys.append(y)

    chaos_fractal_painter(xs, ys, save_path)


# logistic(save_path='fractal/logistic.png')


def martin(save_path=None):
    """https://www.cnblogs.com/WhyEngine/p/4330595.html"""
    sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0
    xs, ys = [], []

    a, b, c = 0.68, 0.75, 0.83
    x, y = 1., 1.
    for t in range(100000):
        x_ = y - sgn(x) * abs(b * x - c) ** 0.5
        y = a - x
        x = x_
        xs.append(x)
        ys.append(y)

    chaos_fractal_painter(xs, ys, save_path)


# martin(save_path='fractal/martin.png')


def ifs(a, rule, save_path=None):
    np.random.seed(0)

    x0, y0 = 1, 1
    xs, ys = [], []

    for _ in tqdm(range(100000)):
        r = np.random.rand()

        i = rule(r)

        x1 = a[i][0] * x0 + a[i][1] * y0 + a[i][4]
        y1 = a[i][2] * x0 + a[i][3] * y0 + a[i][5]

        x0, y0 = x1, y1
        xs.append(x1)
        ys.append(y1)

    chaos_fractal_painter(xs, ys, save_path)


# a = [[0.195, -0.488, 0.344, 0.433, 0.4431, 0.2452, 0.25],
#      [0.462, 0.414, -0.252, 0.361, 0.2511, 0.5692, 0.25],
#      [-0.058, -0.07, 0.453, -0.111, 0.5976, 0.0969, 0.25],
#      [-0.035, 0.07, -0.469, -0.022, 0.4884, 0.5069, 0.2],
#      [-0.637, 0, 0, 0.501, 0.8562, 0.2513, 0.05]]
#
# ifs(a, lambda x: int(x / 0.2), save_path='fractal/ifs0.png')

# a = [[0.03, 0, 0, 0.45, 0, 0, 0.05],
#      [-0.03, 0, 0, -0.45, 0, 0.4, 0.15],
#      [0.56, -0.56, 0.56, 0.56, 0, 0.4, 0.4],
#      [0.56, 0.56, -0.56, 0.56, 0, 0.4, 0.4]]
#
# ifs(a, lambda x: int(x / 0.25), save_path='fractal/ifs1.png')
