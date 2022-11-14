from mpmath import cot

def dihot(a, b, eps):
    n = 0
    while abs(a - b) > eps: 
        c = (float(a) + float(b)) / 2
        beg_value = cot(a) - 0.1
        end_value = cot(c) - 0.1
        print(n, ": a =", round(a, 4), "\tc =", round(c, 4), "\tb =", round(b, 4))
        b1 = b
        if beg_value * end_value < 0:
            b = c
        else: a = c
        print("\nf(a) =", round(beg_value, 4), "\tf(c) =", round(end_value, 4), "\tf(b) =", round(b1, 4))
        n += 1
    
    print("Результат:", round(end_value, 4), "\tc =", round(c, 4))

dihot(4.6, 4.65, 0.005)