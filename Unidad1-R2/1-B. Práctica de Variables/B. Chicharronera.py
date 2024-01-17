import math
a, b, c = map(int, input().split())
discriminante = b**2 - 4*a*c
x1 = (-b + math.sqrt(discriminante)) / (2*a)
x2 = (-b - math.sqrt(discriminante)) / (2*a)
print(f"{x1:.2f} {x2:.2f}")
