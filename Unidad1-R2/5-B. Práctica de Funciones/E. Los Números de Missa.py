### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
def grado_numero_missa(numero):
    def suma_digitos_potencia(numero, potencia):
        return sum(int(digito)**potencia for digito in str(numero))
    for potencia in range(1, 10): 
        suma = suma_digitos_potencia(numero, potencia)
        if suma == numero:
            return potencia
        if suma > numero:
            break
    return -1
entrada = int(input())
resultado = grado_numero_missa(entrada)
print(resultado)
