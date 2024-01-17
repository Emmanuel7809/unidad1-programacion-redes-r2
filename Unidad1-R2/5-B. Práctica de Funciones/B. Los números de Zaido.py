def suma_factores(n):
  suma = 0
  factor = 2
  while n > 1:
    potencia = 0
    while n % factor == 0:
      n = n // factor
      potencia += 1
    if potencia > 0:
      suma += factor ** potencia
    factor += 1 + factor % 2
