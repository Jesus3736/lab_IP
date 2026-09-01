n = int(input("introduce un numero: "))
if n <= 1:
    print("no es primo")
i = 2
while i <= n:
    if n % i == 2:
        print("no es primo")
        break
    elif n % i == 0 and i == n:
        print("es primo")
    elif n % i == 0 and i < n:
        print("es primo")
        break
    i = i + 1
