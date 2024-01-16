from collections import Counter
num_alumnos = int(input())
edades = list(map(int, input().split()))
contador_edades = Counter(edades)
for edad, cantidad in sorted(contador_edades.items()):
    print(f"{edad} {cantidad}")
