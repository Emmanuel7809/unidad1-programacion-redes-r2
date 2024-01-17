import math
sets = input().split()
velocidades_x = []
for set_info in sets:
    V, angulo_ataque, direccion = map(float, set_info.split(','))
    if not direccion:
        angulo_ataque = 180 - angulo_ataque
    angulo_radianes = math.radians(angulo_ataque)
    velocidad_x = V * math.cos(angulo_radianes)
    velocidades_x.append(velocidad_x)
velocidad_promedio_x = math.floor(sum(velocidades_x) / len(velocidades_x))
print(velocidad_promedio_x)
