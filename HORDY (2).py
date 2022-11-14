from math import tan

def f(a):
    return 1/tan(a) - 1

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
    
hord(4.6, 4.65, 0.005)