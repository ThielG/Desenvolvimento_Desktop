from exercicio11 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
numeros = [str(numero) for numero in numeros]
numeros_agrupados = ''.join(numeros)

print(f'Os números da lista agrupados geram a seguinte string: {numeros_agrupados} ')
