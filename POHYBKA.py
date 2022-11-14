def pohybka(x, x1): #   Фунція обрахунку похибок
    absolutn = abs(float(x) - float(x1))    #   Абсолютна
    vidn = abs(float(absolutn) / float(x))  #   Відносна
    print("x =", x, "\tx1 =", x1)
    print("Абсолютна похибка: ", absolutn)
    print("Відносна похибка: ", vidn, "\n")

pohybka(12.251592, 12.14)
pohybka(33000022, 33000019)
pohybka(0.0000730, 0.0000621)