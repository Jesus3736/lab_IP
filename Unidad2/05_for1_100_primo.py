for numero in range(1, 100):
    n = 0
    for d in range(1, numero + 1):
        if numero % d == 0:
            n += 1
    if n == 2:
        print(numero) 