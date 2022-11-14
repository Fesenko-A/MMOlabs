from math import sin
from math import cos

def nuton(a, eps):
    x0 = 0
    xn = a
    fx = 0
    fpx = 0
    n = 0

    while abs(xn - x0) > eps:
        x0 = xn
        fx = x0 * x0 * cos(2 * x0) + 0.2
        fpx = 2 * x0 * cos(2 * x0) - 2 * x0 * x0 * sin(2 * x0)
        xn = x0 - fx / fpx
        print("n =", n, "\tx =", n, "=", round(x0, 4), "\tx", (n + 1), "=", round(xn, 4), "\nf(x) =", round(fx, 4), "\tf'(x) =", round(fpx, 4), "\tdx =", round(abs(xn - x0), 4), "\n")
        n += 1
    
    print("Результат:", xn)

nuton(0.88, 0.005)