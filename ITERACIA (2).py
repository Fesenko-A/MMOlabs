from mpmath import cot

def iter(a, eps):
    x0 = 0
    xn = a
    n = 0
    while (True):
        x0 = xn
        xn = cot(x0) - 0.1 + x0
        print("n:", n, "\tx", n, "=", round(-x0, 5), "\tx", (n + 1), "=", round(-xn, 5))
        n += 1
        if (abs(xn - x0) > eps):
            break

iter(4.6, 0.005)