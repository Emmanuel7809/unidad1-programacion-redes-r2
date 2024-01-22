### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
def find_fibonacci_term(N):
    a, b = 0, 1
    term = 1
    while b < N:
        a, b = b, a + b
        term += 1
    return b
N = int(input())
resultado = find_fibonacci_term(N)
print(resultado)
