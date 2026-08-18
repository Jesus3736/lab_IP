numero = 8

if numero == 0:
    print("0")
    
hexadecimal = ""
letras = "0123456789ABCDEF"

while numero > 0:
    residuo = numero % 16 
    hexadecimal = letras[residuo] + hexadecimal  
    numero = numero // 16      
    
print(hexadecimal)
