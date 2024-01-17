cadena = input().split()
resultado = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        resultado += cadena[i].lower() + " "
    else:
        resultado += cadena[i].upper() + " "

print(resultado.rstrip())
