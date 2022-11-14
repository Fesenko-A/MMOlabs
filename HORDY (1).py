from math import cos

def f(a):
    return a * a * cos(2 * a) + 0.2

def hord(a1, b, eps):
    a = 0
    x = a1
    n = 0
    while abs(a1 - a) > eps:
        a = a1
        a1 = a - (f(a) * (b - a)) / (f(b) - f(a))
        print("n =", n, "\tx =", round(a, 4), "\tx", (n + 1), "=", round(a1, 4), "\tdx =", round(abs(x - a), 4), "\n")
        n += 1
        
    print("Результат: ", a1)
    
hord(0.88, 0.98, 0.005)