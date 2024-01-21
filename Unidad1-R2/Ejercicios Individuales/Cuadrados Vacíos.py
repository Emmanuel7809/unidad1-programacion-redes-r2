def construir_cuadrado(lado):
    if lado == 1:
        print('*')
    else:
        print('*' * lado)
        for _ in range(lado - 2):
            print('*' + ' ' * (lado - 2) + '*')
        if lado > 1:
            print('*' * lado)

lado = int(input())
construir_cuadrado(lado)
