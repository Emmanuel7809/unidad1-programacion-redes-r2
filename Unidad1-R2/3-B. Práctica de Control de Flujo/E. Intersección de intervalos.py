### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
def existe_interseccion(intervalo1_inicio, intervalo1_fin, intervalo2_inicio, intervalo2_fin):
    if intervalo1_fin < intervalo2_inicio or intervalo2_fin < intervalo1_inicio:
        return 0
    else:
        return 1
entrada = input().split()
intervalo1_inicio, intervalo1_fin, intervalo2_inicio, intervalo2_fin = map(int, entrada)
resultado = existe_interseccion(intervalo1_inicio, intervalo1_fin, intervalo2_inicio, intervalo2_fin)
print(resultado)
