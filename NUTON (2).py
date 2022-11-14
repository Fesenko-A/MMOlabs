from math import tan
from math import sin

def nuton(a, eps):
    x0 = 0
    xn = a
    fx = 0
    fpx = 0
    n = 0

    while abs(xn - x0) > eps:
        x0 = xn
        fx = 1 / tan(x0) - 0.1
        fpx = - (1 / sin(x0) ** 2)
        xn = x0 - fx / fpx
        print("n =", n, "\tx =", round(x0, 4), "\tx", (n + 1), "=", round(xn, 4), "\nf(x) =", round(fx, 4), "\tf'(x) =", round(fpx, 4), "\tdx =", round(abs(xn - x0), 4), "\n")
        n += 1

    print("Результат", xn)

nuton(4.6, 0.005)