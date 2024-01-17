def es_capicua(numero):
    return str(numero) == str(numero)[::-1]
def obtener_capicua(num):
    while not es_capicua(num):
        num += int(str(num)[::-1])
    return num
entrada = int(input())
resultado = obtener_capicua(entrada)
print(resultado)
