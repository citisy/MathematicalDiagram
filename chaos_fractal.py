import numpy as np
from PIL import Image
from tqdm import tqdm
from moviepy.editor import ImageSequenceClip
import matplotlib.pyplot as plt

mandelbrot_set = 0
julia_set = 1


def fractal_set(xaxis, yaxis, size, r=2, maxiter=100,
                fractal_type=mandelbrot_set, c=complex(0, 0), img_save_path=None):
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

    for idx1, i in tqdm(enumerate(r1)):
        for idx2, j in enumerate(r2):
            if fractal_type == mandelbrot_set:
                img_array[idx2, idx1] = mandelbrot(complex(i, j))
            else:
                img_array[idx2, idx1] = julia(complex(i, j))

    img = Image.fromarray(img_array)

    if img_save_path:
        img.save(img_save_path)

    # img.show()

    return img_array


def logistic(img_save_path=None):
    """http://wiki.swarma.net/index.php/Logistic%E6%98%A0%E5%B0%84"""
    us, xs = [], []
    for u in tqdm(np.arange(0.9, 4, 0.002)):
        for x in np.arange(0.1, 0.9, 0.02):
            for t in range(1000):
                x = u * x * (1 - x)
            us.append(u)
            xs.append(x)

    plt.figure(figsize=(12, 12))
    plt.scatter(us, xs, s=1, marker=',')

    if img_save_path:
        plt.savefig(img_save_path)

    # plt.show()


def martin(img_save_path=None):
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

    plt.figure(figsize=(12, 12))
    plt.scatter(xs, ys, s=1, marker=',')

    if img_save_path:
        plt.savefig(img_save_path)

    # plt.show()


def newton(img_save_path=None):
    """https://www.cnblogs.com/WhyEngine/p/4069145.html"""

    xs, ys = [], []
    eps = 1e-2
    for x0 in tqdm(np.arange(-1, 1, 0.005)):
        for y0 in np.arange(-1, 1, 0.005):
            x, y = x0, y0
            for t in range(64):
                xx, yy = x ** 2, y ** 2
                d = 3 * ((xx - yy) ** 2) + 4 * xx * yy
                if abs(d) < eps:
                    if d > 0:
                        d = eps
                    else:
                        d = -eps
                x_ = x
                x = 1 / 3 * x + (xx - yy) / d
                y = 1 / 3 * y - 2 * x_ * y / d
            if x < 0:
                x, y = 0, 0
            xs.append(x)
            ys.append(y)

    # plt.figure(figsize=(12, 12))
    plt.scatter(xs, ys, s=1, marker=',')

    if img_save_path:
        plt.savefig(img_save_path)

    plt.show()


if __name__ == '__main__':
    # fractal_set((-2.0, 0.5), (-1.25, 1.25), (1000, 1000), img_save_path='fractal/mandelbrot_set.png')
    # fractal_set((.275, .28), (.006, .01), (1000, 1000), img_save_path='fractal/elephant_valley.png')
    # fractal_set((-.09, -.086), (.654, .657), (1000, 1000), img_save_path='fractal/triple_spiral_valley.png')
    # fractal_set((-.75, -.747), (.099, .102), (1000, 1000), img_save_path='fractal/seahorse_valley.png')

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

    # logistic(img_save_path='fractal/logistic.png')

    # martin(img_save_path='fractal/martin.png')

    newton()
