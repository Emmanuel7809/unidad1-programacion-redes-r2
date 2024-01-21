entrada = input()
if len(entrada) < 2:
    print("Por favor, ingrese un número con al menos dos dígitos.")
else:
    invertido = int(entrada[::-1])
    print(invertido)
