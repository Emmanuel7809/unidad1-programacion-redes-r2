def imprimir_multiplos(a, b):
    for i in range(a, b + 1, a):
        print(i, end=" ")
entrada = input().split()
a, b = map(int, entrada)
imprimir_multiplos(a, b)
