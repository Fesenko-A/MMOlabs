from math import tan
from math import sin

def f(a):
    return 1/tan(a) - 1

def hord(a1, b, eps):
    z_prev = 0
    z_cur = a1
    x_prev = 0
    x_cur = a1
    func = 0
    func_deriv = 0
    n = 0
    while True:
        x_prev = z_cur
        z_prev = x_cur
        func = f(x_prev)
        func_deriv = -(1 / sin(x_prev) * sin(x_prev))
        x_cur = x_prev - func / func_deriv
        z_cur = z_prev - (f(z_prev) * (b - z_prev)) / (f(b) - f(x_prev))
        print("n =", n, "\tДотична x =", round(x_cur, 4), "\tХорда x =", round(z_cur, 4), "\tdx =", round(abs(x_cur - z_cur), 4), "\n")
        n += 1
        if abs(x_cur - z_cur) > eps:
            break
        
    print("Результат: ", (x_cur + z_cur) / 2.0)
    
hord(4.6, 4.65, 0.005)