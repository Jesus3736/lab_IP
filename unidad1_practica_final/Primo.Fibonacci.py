n = int(input("Introduce un número: "))
es_primo = True
if n <= 1:
    es_primo = False
if n > 1:
    i = 2
    while i < n:
        if n % i == 0:
            es_primo = False
        i = i + 1
if es_primo == True:
    print("Es primo")

if es_primo == False:
    print("No es primo")
a = 0
b = 1
while a < n:
    siguiente = a + b
    a = b
    b = siguiente
if a == n:
    print("Está en Fibonacci")

if a != n:
    print("No está en Fibonacci")