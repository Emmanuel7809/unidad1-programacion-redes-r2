### Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes Unidad 1 Recuperacion 2
from datetime import datetime
def calcular_diferencia_entre_fechas(a, b, c, p, q, r):
    fecha_inicial = datetime(c, b, a)
    fecha_final = datetime(r, q, p)
    diferencia = fecha_final - fecha_inicial
    return abs(diferencia.days)
fecha1 = input("Ingrese la primera fecha (a b c): ").split()
fecha2 = input("Ingrese la segunda fecha (p q r): ").split()
a, b, c = map(int, fecha1)
p, q, r = map(int, fecha2)
diferencia_dias = calcular_diferencia_entre_fechas(a, b, c, p, q, r)
print(diferencia_dias)
