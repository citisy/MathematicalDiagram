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
        z = 0
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

    img.show()

    return img_array


# colorful_fractal_set((-2.0, 0.5), (-1.25, 1.25), (1000, 1000), save_path='fractal/mandelbrot_set.png')
# colorful_fractal_set((.275, .28), (.006, .01), (1000, 1000), save_path='fractal/elephant_valley.png')
# colorful_fractal_set((-.09, -.086), (.654, .657), (1000, 1000), save_path='fractal/triple_spiral_valley.png')
# colorful_fractal_set((-.75, -.747), (.099, .102), (1000, 1000), save_path='fractal/seahorse_valley.png')

# from moviepy.editor import ImageSequenceClip
# n = 60
# seq = []
# for i in range(n):
#     theta = 2 * np.pi / n * i
#     c = -(0.835 - 0.1 * np.cos(theta)) - (0.2321 + 0.1 * np.sin(theta)) * 1j
#     img = colorful_fractal_set((-1.5, 1.5), (-1.5, 1.5), (500, 500), c=c,
#                       fractal_type=julia_set)
#     seq.append(img)
# clip = ImageSequenceClip(seq, fps=10)
# clip.write_gif('fractal/julia_set.gif', fps=10)


def mandelbrot():
    xs, ys = [], []
    for x in tqdm(np.linspace(-2.0, 0.5, 1000)):
        for y in np.linspace(-1.25, 1.25, 1000):
            c = complex(x, y)
            z = 0
            for i in range(100):
                if abs(z) > 2:
                    break
                z = z ** 2 + c
            else:
                xs.append(x)
                ys.append(y)

    chaos_fractal_painter(xs, ys, draw_args={
        # 'save_path': 'fractal/mandelbrot.png'
    })


# mandelbrot()


def julia():
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

    chaos_fractal_painter(xs, ys, draw_args={
        # 'save_path': 'fractal/julia.png'
    })


# julia()


def newton_iterate():
    """https://www.cnblogs.com/WhyEngine/p/4069145.html
    https://www.douban.com/note/230496472/"""

    xs, ys = [], []
    eps = 1e-6
    for x0 in tqdm(np.linspace(-1, 1, 500)):
        for y0 in np.linspace(-1, 1, 500):
            z = complex(x0, y0)
            for t in range(1000):
                if z == 0:
                    break
                y = z - (z ** 3 - 1) / (3 * z ** 2)
                if abs(y - z) < eps:
                    if abs(y - 1) < eps:
                        xs.append(x0)
                        ys.append(y0)
                    break
                z = y

    chaos_fractal_painter(xs, ys, draw_args={
        # 'save_path': 'fractal/newton_iterate.png'
    })


# newton_iterate()


def logistic():
    """http://wiki.swarma.net/index.php/Logistic%E6%98%A0%E5%B0%84"""
    xs, ys = [], []
    for x in tqdm(np.linspace(0.9, 4, 1000)):
        for y in np.linspace(0.1, 0.9, 100):
            for t in range(1000):
                y = x * y * (1 - y)
            xs.append(x)
            ys.append(y)

    chaos_fractal_painter(xs, ys, draw_args={
        # 'save_path': 'fractal/logistic.png'
    })


# logistic()


def martin():
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

    chaos_fractal_painter(xs, ys, draw_args={
        # 'save_path': 'fractal/martin.png'
    })


# martin()


def ifs(ifs_code, draw_args=dict()):
    """https://www.cnblogs.com/WhyEngine/p/4069166.html"""
    np.random.seed(0)

    x0, y0 = 1, 1
    xs, ys = [], []

    for _ in tqdm(range(100000)):
        r = np.random.rand()

        for i in ifs_code:
            if r < i[-1]:
                code = i
                break
        else:
            code = ifs_code[-1]

        a, b, c, d, e, f = code[:-1]

        x1 = a * x0 + b * y0 + e
        y1 = c * x0 + d * y0 + f

        x0, y0 = x1, y1
        xs.append(x1)
        ys.append(y1)

    chaos_fractal_painter(xs, ys, draw_args)


# ifs_code = [[0.195, -0.488, 0.344, 0.433, 0.4431, 0.2452, 0.25],
#             [0.462, 0.414, -0.252, 0.361, 0.2511, 0.5692, 0.5],
#             [-0.058, -0.07, 0.453, -0.111, 0.5976, 0.0969, 0.75],
#             [-0.035, 0.07, -0.469, -0.022, 0.4884, 0.5069, 0.95],
#             [-0.637, 0, 0, 0.501, 0.8562, 0.2513, 1]]
#
# ifs(ifs_code, draw_args={
#     # 'save_path': 'fractal/ifs0.png'
# })

# ifs_code = [[0.03, 0, 0, 0.45, 0, 0, 0.05],
#             [-0.03, 0, 0, -0.45, 0, 0.4, 0.2],
#             [0.56, -0.56, 0.56, 0.56, 0, 0.4, 0.6],
#             [0.56, 0.56, -0.56, 0.56, 0, 0.4, 1]]
#
# ifs(ifs_code, draw_args={
#     # 'save_path': 'fractal/ifs1.png'
# })

# ifs_code = [[.5, 0, 0, .5, 0, 0, 1. / 3.],
#             [.5, 0, 0, .5, .5, 0, 2. / 3],
#             [.5, 0, 0, .5, .25, .5, 1]]
#
# ifs(ifs_code, draw_args={
#     # 'save_path': 'fractal/ifs2.png'
# })

# ifs_code = [[0, 0, 0, .16, 0, 0, .01],
#             [.2, -.26, .23, .22, 0, 1.6, .08],
#             [-.15, .28, .26, .24, 0, .44, .15],
#             [.85, .04, .04, .85, 0, 1.6, 1]]
#
# ifs(ifs_code, draw_args={
#     # 'save_path': 'fractal/ifs3.png'
# })
