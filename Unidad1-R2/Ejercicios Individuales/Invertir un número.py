### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
entrada = input()
if len(entrada) < 2:
    print("Por favor, ingrese un número con al menos dos dígitos.")
else:
    invertido = int(entrada[::-1])
    print(invertido)
