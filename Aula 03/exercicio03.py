from time import sleep

numero = int(input('Informe um número natural: '))
contador = 0

while contador <= 10:
    print(f'n° {numero}')
    numero += 1
    contador += 1
    sleep(0.4)
