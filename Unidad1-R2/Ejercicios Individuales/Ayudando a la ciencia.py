def CelsiusaFarenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
def CelsiusaKelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
def OperacionTemperaturas(celsius):
    farenheit = CelsiusaFarenheit(celsius)
    kelvin = CelsiusaKelvin(celsius)
    operacion = 5 * (1.5 * ((farenheit / 2) + (kelvin / 4)))
    return farenheit, kelvin, operacion
celsius = float(input())
resultados = OperacionTemperaturas(celsius)
print("{:.2f} {:.2f} {:.2f}".format(resultados[0], resultados[1], resultados[2]))
