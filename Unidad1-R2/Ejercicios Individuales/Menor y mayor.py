### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
a, b, c, d = map(int, input().split())
suma1 = a + b
suma2 = a + c
suma3 = a + d
suma4 = b + c
suma5 = b + d
suma6 = c + d
menor_suma = min(suma1, suma2, suma3, suma4, suma5, suma6)
mayor_suma = max(suma1, suma2, suma3, suma4, suma5, suma6)
print(menor_suma, mayor_suma)
