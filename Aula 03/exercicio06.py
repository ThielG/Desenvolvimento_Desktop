from funcao01 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
print(f'A lista de números inicial é {numeros}')

print("Índice | Número")
print("----------------")
for i in range(len(numeros)):
    print(f'{i:6} | {numeros[i]:6}')
