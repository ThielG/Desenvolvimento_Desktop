import random

numeros = []

for _ in range(10):
    numeros.append(random.randint(20, 1580))

numeros.sort()

print(numeros)
