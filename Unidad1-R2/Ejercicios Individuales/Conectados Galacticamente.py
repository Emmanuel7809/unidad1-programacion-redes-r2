def suma_digitos(numero):
    return sum(int(digito) for digito in str(abs(numero)))

def conectados_galacticamente():
    try:
        M = int(input("Ingrese el primer número entero (M): "))
        N = int(input("Ingrese el segundo número entero (N): "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        return

    print(f"{M},{N}")

    if abs(M - N) <= 15:
        print("Conectados Galacticamente")
    else:
        print("Ni se topan")

conectados_galacticamente()
