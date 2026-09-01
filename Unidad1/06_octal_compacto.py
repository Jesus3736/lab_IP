numero = 8 #
if numero == 0: print("0")
octal = ""
while numero > 0: octal = str(numero % 8) + octal; numero = numero // 8
print(octal)
