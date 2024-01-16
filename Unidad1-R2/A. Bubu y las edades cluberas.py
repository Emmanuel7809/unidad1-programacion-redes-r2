edades = input().split()
edades_unicas = sorted(set(edades), key=int, reverse=True)
print(edades_unicas)
