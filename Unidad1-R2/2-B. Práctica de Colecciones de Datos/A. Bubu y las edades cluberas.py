### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
edades = input().split()
edades_unicas = sorted(set(edades), key=int, reverse=True)
print(edades_unicas)
