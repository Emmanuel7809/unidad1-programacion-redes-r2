def sumar_dias(a, b, c, n):
    from datetime import datetime, timedelta
    fecha_inicial = datetime(c, b, a)
    fecha_resultante = fecha_inicial + timedelta(days=n)
    return fecha_resultante.day, fecha_resultante.month, fecha_resultante.year
a, b, c, n = map(int, input().split())
resultado = sumar_dias(a, b, c, n)

print(f"{resultado[0]} {resultado[1]} {resultado[2]}")
