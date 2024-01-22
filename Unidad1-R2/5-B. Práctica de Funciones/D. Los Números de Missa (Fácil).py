### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
def es_numero_missa(n, k):
    def obtener_digitos(numero):
        return [int(digito) for digito in str(numero)]
    suma_digitos_potencia_k = sum(digito**k for digito in obtener_digitos(n))
    return "Simón Missa" if suma_digitos_potencia_k == n else "Nelpas Mijo"
entrada = input().split()
n, k = map(int, entrada)
resultado = es_numero_missa(n, k)
print(resultado)
