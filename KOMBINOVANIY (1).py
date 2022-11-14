from math import cos
from math import sin

def f(a):
    return a * a * cos(2 * a) + 0.2

def hord(a1, b, eps):
    z_prev = 0
    z_cur = a1
    x_prev = 0
    x_cur = a1
    func = 0
    func_deriv = 0
    n = 0
    while abs(x_cur - z_cur) > eps:
        x_prev = z_cur
        z_prev = x_cur
        func = f(x_prev)
        func_deriv = 2 * x_prev * cos(2 * x_prev) - 2 * x_prev * x_prev * sin(2 * x_prev)
        x_cur = x_prev - func / func_deriv
        z_cur = z_prev - (f(z_prev) * (b - z_prev)) / (f(b) - f(x_prev))
        print("n =", n, "\tДотична x =", round(x_cur, 4), "\tХорда x =", round(z_cur, 4), "\tdx =", round(abs(x_cur - z_cur), 4), "\n")
        n += 1
        
    print("Результат: ", (x_cur + z_cur) / 2.0)
    
hord(0.88, 0.98, 0.005)