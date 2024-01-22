### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def combinaciones(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
nombres = input().split()
nombres = [nombre for nombre in nombres if nombre not in ["Ricardo", "Mirón"]]
num_personas = len(nombres)
num_squads = combinaciones(num_personas, 4)
print(num_squads)
