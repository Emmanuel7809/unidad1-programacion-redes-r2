### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
N = int(input())
conjunto = list(map(int, input().split()))
creciente = sorted(conjunto)
decreciente = sorted(conjunto, reverse=True)
print(" ".join(map(str, creciente)))
print(" ".join(map(str, decreciente)))
