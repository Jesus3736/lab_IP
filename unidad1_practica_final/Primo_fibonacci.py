n = int(input("introduce un numero: "))
if n <= 1:
    print("no es primo")
else:
    i = 2
    while i <= n:
        if n % i == 0 and i < n:
            print("No es primo")
            break
        elif n % i == 0 and i == n:
            print("Es primo")
            break
        i = i + 1
a = 0
b = 1
while a < n:
    siguiente = a + b
    a = b
    b = siguiente 
if a == n:
    print("Está en Fibonacci")
else:
    print ("no esta en Fibonacci")  





        