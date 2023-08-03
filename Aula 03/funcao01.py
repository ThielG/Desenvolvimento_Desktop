import random

def gera_numeros_aleatorios(quantidade) -> list:
    numeros_aleatorios = []

    for _ in range(quantidade):
        numeros_aleatorios.append(random.randint(20, 1580))

    return numeros_aleatorios
