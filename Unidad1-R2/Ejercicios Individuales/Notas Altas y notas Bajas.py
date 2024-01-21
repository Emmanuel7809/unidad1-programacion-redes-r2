def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 2)
n = int(input())
calificaciones = list(map(int, input().split()))
calificaciones_ordenadas = sorted(calificaciones)
mediana = calificaciones_ordenadas[(n + 1) // 2 - 1]
notas_bajas = calificaciones_ordenadas[:(n + 1) // 2 - 1]
notas_altas = calificaciones_ordenadas[(n + 1) // 2:]
promedio_bajas = calcular_promedio(notas_bajas)
promedio_altas = calcular_promedio(notas_altas)
print(" ".join(map(str, calificaciones_ordenadas)))
print(mediana)
print(f"{promedio_bajas:.2f}")
print(f"{promedio_altas:.2f}")
