from math import cos

def dihot(a, b, eps):
    n = 0
    while abs(a - b) > eps:
        c = (float(a) + float(b)) / 2
        beg_value = a * a * cos(2 * a) + 0.2
        end_value = c * c * cos(2 * c) + 0.2
        print(n, ": a =", round(a, 4), "\tc =", round(c, 4), "\tb =", round(b, 4))
        b1 = b
        if beg_value * end_value < 0:
            b = c
        else: a = c
        print("\nf(a) =", round(beg_value, 4), "\tf(c) =", round(end_value, 4), "\tf(b) =", round(b1, 4))
        n += 1
    
    print("Результат:", round(end_value, 4), "\tc =", round(c, 4))

dihot(0.88, 0.98, 0.005)