import math

area = float(input('Informe o tamanho da área a ser pintada (em metros quadrados): '))

litros = area / 3

quantidade = math.ceil(litros / 18)

preco = 80.00
total = round(quantidade * preco, 2)

print(f'\nQuantidade de latas de tinta a serem compradas: {quantidade}. \nPreço total: R$ {total}')
