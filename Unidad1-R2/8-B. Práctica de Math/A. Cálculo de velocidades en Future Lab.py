import math
sets = input().split()
velocidades = []
for set_info in sets:
    L, densidad_aire, coeficiente_levantamiento, superficie_alar = map(float, set_info.split(','))
    velocidad = math.sqrt((2 * L) / (densidad_aire * coeficiente_levantamiento * superficie_alar))
    velocidades.append(velocidad)
velocidad_promedio = math.ceil(sum(velocidades) / len(velocidades))
print(velocidad_promedio)
