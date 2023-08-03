from funcao01 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
print(f'Lista de números: {numeros}.')

for numero in numeros:
    if numero % 5 == 0:
        print(f'O número {numero} é multiplo de 5.')
    elif numero > 95 and numero < 150:
        print(f'O número {numero} está localizado entre os números 95 e 150.')
        pass
    elif numero > 1500:
        print('Fim do loop.')
        break
    else:
        print(f'O número {numero} não se encaixa em nenhuma condicional.')
        continue
