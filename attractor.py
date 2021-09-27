"""https://chaoticatmospheres.com/mathrules-strange-attractors"""
from utils import *


def lorenz(x, y, z, s=10, r=28, b=2.667):
    dx = s * (y - x)
    dy = r * x - y - x * z
    dz = x * y - b * z
    return dx, dy, dz


# attractor_painter(lorenz, save_path='attractor/lorenz.png')


def lu_chen(x, y, z, a=-10, b=-4, c=18.1):
    dx = -(a * b * x) / (a + b) - y * z + c
    dy = a * y + x * z
    dz = b * z + x * y
    return dx, dy, dz


# attractor_painter(lu_chen, save_path='attractor/lu_chen.png')


def lorenz1(x, y, z, a=0.1, b=4, c=14, d=0.08):
    dx = -a * x + y ** 2 - z ** 2 + a * c
    dy = x * (y - b * z) + d
    dz = z + x * (b * y + z)
    return dx, dy, dz


# attractor_painter(lorenz1, save_path='attractor/lorenz1.png')


def genesio_tesi(x, y, z, a=0.44, b=1.1, c=1.):
    dx = y
    dy = z
    dz = -c * x - b * y - a * z + x ** 2
    return dx, dy, dz


# attractor_painter(genesio_tesi, save_path='attractor/genesio_tesi.png')


def chen_lee(x, y, z, a=5, b=-10, c=-0.38):
    dx = a * x - y * z
    dy = b * y + x * z
    dz = c * z + x * y / 3
    return dx, dy, dz


# attractor_painter(chen_lee, dt=1e-4, n_steps=int(1e6), save_path='attractor/chen_lee.png')


def nose_hoover(x, y, z, a=1.5):
    dx = y
    dy = -x + y * z
    dz = a - y ** 2
    return dx, dy, dz


# attractor_painter(nose_hoover, save_path='attractor/nose_hoover.png')


def chua(x, y, z, a=15.6, b=1, c=25.58, d=-1, e=0):
    gx = e * x + (d + e) * (abs(x + 1) - abs(x - 1))
    dx = a * (y - x - gx)
    dy = b * (x - y + z)
    dz = -c * y
    return dx, dy, dz


# attractor_painter(chua, save_path='attractor/chua.png')


def newton_leipnik(x, y, z, a=0.4, b=0.175):
    dx = -a * x + y + 10 * y * z
    dy = -x - 0.4 * y + 5 * x * z
    dz = b * z - 5 * x * y
    return dx, dy, dz


# attractor_painter(newton_leipnik, dt=1e-4, n_steps=int(1e6), save_path='attractor/newton_leipnik.png')


def thomas(x, y, z, a=0.19):
    dx = a * x + sin(y)
    dy = -a * y + sin(z)
    dz = -a * z + sin(x)
    return dx, dy, dz


# attractor_painter(thomas, save_path='attractor/thomas.png')


def shimizu(x, y, z, a=0.75, b=0.45):
    dx = y
    dy = (1 - z) * x - a * y
    dz = x ** 2 - b * z
    return dx, dy, dz


# attractor_painter(shimizu, save_path='attractor/shimizu.png')


def halvorsen(x, y, z, a=1.4):
    dx = -a * x - 4 * y - 4 * z - y ** 2
    dy = -a * y - 4 * z - 4 * x - z ** 2
    dz = -a * z - 4 * x - 4 * y - x ** 2
    return dx, dy, dz


# attractor_painter(halvorsen, dt=1e-4, n_steps=int(1e6), start_xyz=(0.1, -0.1, -0.1), save_path='attractor/halvorsen.png')


def yu_wang(x, y, z, a=10, b=40, c=2, d=2.5):
    dx = a * (y - x)
    dy = b * x - c * x * z
    dz = np.exp(x * y) - d * z
    return dx, dy, dz


# attractor_painter(yu_wang, save_path='attractor/yu_wang.png')


def lorenz2(x, y, z, a=0.9, b=5, c=9.9, d=1):
    dx = -a * x + y ** 2 - z ** 2 + a * c
    dy = x * (y - b * z) + d
    dz = -z + x * (b * y + z)
    return dx, dy, dz


# attractor_painter(lorenz2, save_path='attractor/lorenz2.png')


def four_wing(x, y, z, a=4, b=6, c=0.1, d=5, e=1):
    dx = a * x - b * y * z
    dy = -c * y + x * z
    dz = e * x - d * z + x * z
    return dx, dy, dz


# attractor_painter(four_wing,  save_path='attractor/four_wing.png')


def anishchenko_astakhov(x, y, z, a=1.2, b=0.5):
    dx = a * x + y - x * z
    dy = -x
    dz = -b * z + b * np.signbit(x) * x ** 2
    return dx, dy, dz


# attractor_painter(anishchenko_astakhov, save_path='attractor/anishchenko_astakhov.png')


def lorenz_stenflo(x, y, z, w, a=2, b=0.7, c=26, d=1.5):
    dx = a * (y - x) + d * w
    dy = x * (c - z) - y
    dz = x * y - b * z
    dw = -x - a * w
    return (dx, dy, dz), (dw,)


# attractor_painter(lorenz_stenflo, 0.1, save_path='attractor/lorenz_stenflo.png')


def arneodo(x, y, z, a=-5.5, b=3.5, c=-1):
    dx = y
    dy = z
    dz = -a * x - b * y - z + c * x ** 3
    return dx, dy, dz


# attractor_painter(arneodo, save_path='attractor/arneodo.png')


def bouali(x, y, z, a=0.3, b=1):
    dx = x * (4 - y) + a * z
    dy = -y * (1 - x ** 2)
    dz = -x * (1.5 - b * z) - 0.05 * z
    return dx, dy, dz


# attractor_painter(bouali, save_path='attractor/bouali.png')


def dadras(x, y, z, a=3, b=2.7, c=1.7, d=2, e=9):
    dx = y - a * x + b * y * z
    dy = c * y - x * z + z
    dz = d * x * y - e * z
    return dx, dy, dz


# attractor_painter(dadras, save_path='attractor/dadras.png')


def dequan_li(x, y, z, a=40, b=1.833, c=0.16, d=0.65, e=55, f=20):
    dx = a * (y - x) + c * x * z
    dy = e * x + f * y - x * z
    dz = b * z + x * y - d * x ** 2
    return dx, dy, dz


# attractor_painter(dequan_li, dt=1e-4, save_path='attractor/dequan_li.png')


def rucklidge(x, y, z, a=2, b=6.7):
    dx = -a * x + b * y - y * z
    dy = x
    dz = -z + y ** 2
    return dx, dy, dz


# attractor_painter(rucklidge, save_path='attractor/rucklidge.png')


def finance(x, y, z, a=0.001, b=0.2, c=1.1):
    dx = (1 / b - a) * x + z + x * y
    dy = -b * y - x ** 2
    dz = -x - c * z
    return dx, dy, dz


# attractor_painter(finance, save_path='attractor/finance.png')


def burke(x, y, z, a=10, b=4.272):
    dx = -a * (x + y)
    dy = -y - a * x * z
    dz = a * x * y + b
    return dx, dy, dz


# attractor_painter(burke, save_path='attractor/burke.png')


def qi(x, y, z, w, a=3, b=1, c=1, d=1):
    dx = a * (y - x) + y * z * w
    dy = b * (x + y) - x * z * w
    dz = -c * z + x * y * w
    dw = -d * w + x * y * z
    return (dx, dy, dz), (dw,)


# attractor_painter(qi, 0.1,  save_path='attractor/qi.png')


def chen_celikovsky(x, y, z, a=36, b=3, c=20):
    dx = a * (y - x)
    dy = -x * z + c * y
    dz = x * y - b * z
    return dx, dy, dz


# attractor_painter(chen_celikovsky, save_path='attractor/chen_celikovsky.png')


def three_scroll(x, y, z, a=50, b=0.833, c=0.5, d=0.65, e=20):
    dx = a * (y - x) + c * x * z
    dy = e * x - x * z
    dz = b * z + x * y - d * x ** 2
    return dx, dy, dz


# attractor_painter(three_scroll, save_path='attractor/three_scroll.png')


def aizawa(x, y, z, a=0.929200, b=0.731500, c=0.6, d=3.5, e=0.25, f=1.081599):
    dy = d * x + (z - b) * y
    dx = (z - b) * x - dy
    dz = c + a * z - z ** 2 / 3 - (x ** 2 + y ** 2) * (1 + e * z) + f * z * x ** 2
    return dx, dy, dz


# attractor_painter(aizawa, start_xyz=(0.1, -0.5, 0.3), save_path='attractor/aizawa.png')


def sakarya(x, y, z, a=0.4, b=0.3):
    dx = -x + y + y * z
    dy = -x - y + a * x * z
    dz = z - b * x * y
    return dx, dy, dz


# attractor_painter(sakarya, save_path='attractor/sakarya.png')


def wimol_banlue(x, y, z, a=2):
    dx = y - x
    dy = -z * np.tan(x)
    dz = -a + x * y + abs(y)
    return dx, dy, dz


# attractor_painter(wimol_banlue, start_xyz=(1, 1, 1), save_path='attractor/wimol_banlue.png')


def qi_chen(x, y, z, a=38, b=2.6667, c=80):
    dx = a * (y - x) + y * z
    dy = c * x + y - x * z
    dz = x * y - b * z
    return dx, dy, dz


# attractor_painter(qi_chen, save_path='attractor/qi_chen.png')


def hadley(x, y, z, a=0.4, b=4, c=5, d=1):
    dx = -y ** 3 - z ** 3 - a * x + a * c
    dy = x * y - b * x * z - y + d
    dz = b * x * y + x * z - z
    return dx, dy, dz


# attractor_painter(hadley, save_path='attractor/hadley.png')


def russler(x, y, z, a=0.2, b=0.2, c=5.7):
    dx = -(y + z)
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz


# attractor_painter(russler, save_path='attractor/russler.png')


def liu_chen(x, y, z, a=1.897, b=-3.78, c=-14, d=-11.3, e=-1, f=5.58, g=1):
    dx = a * y + b * x + c * y * z
    dy = d * y - z + e * x * z
    dz = f * z + g * x * y
    return dx, dy, dz


# attractor_painter(liu_chen, save_path='attractor/liu_chen.png')


def rayleigh_benard(x, y, z, a=-3.271399, b=5.279099, c=12.450301):
    dx = -a * x + a * y
    dy = c * x - y - x * z
    dz = x * y - b * z
    return dx, dy, dz

# attractor_painter(rayleigh_benard, save_path='attractor/rayleigh_benard.png')
