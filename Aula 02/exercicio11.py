quantidade = int(input('Informe o tamanho da lista: '))
contador = 1
lista = []

while contador <= quantidade:
    if contador % 2 == 0:
        lista.append(contador)
        contador += 1
    elif contador % 2 != 0:
        contador += 1
        continue

print(f'Em uma lista do tamanho de {quantidade}, os seguintes itens são pares: {lista}.')
