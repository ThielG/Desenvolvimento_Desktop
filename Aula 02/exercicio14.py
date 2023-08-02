quantidade = int(input('Informe o tamanho da lista: '))
contador = 1
lista = []

while contador <= quantidade:
    numero = int(input(f'Informe o {quantidade}° número: '))
    if numero % 2 == 0:
        lista.append(numero)
        contador += 1
    else:
        contador += 1
        continue

print(f'\nDos números informados, os seguintes são pares: {lista}.')
