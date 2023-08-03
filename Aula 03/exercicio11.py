import random as r

def gera_numeros_aleatorios(quantidade) -> list:
    numeros = []

    for _ in range(quantidade):
        numeros.append(r.randint(20, 1580))
    return numeros
