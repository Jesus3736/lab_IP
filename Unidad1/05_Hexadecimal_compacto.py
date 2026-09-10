numero = 8# Pedimos al usuario que ingrese un número
hexadecimal = ""# Creamos una cadena vacía para guardar el resultado en hexadecimal
letras = "0123456789ABCDEF"# Aquí están los símbolos que usamos en hexadecimal (0-9 y A-F)
while numero > 0:
    hexadecimal = letras[numero % 16] + hexadecimal# Dividimos el número entre 16 repetidamente para obtener cada dígito
    numero = numero // 16
print(hexadecimal)# Mostramos el resultado final

