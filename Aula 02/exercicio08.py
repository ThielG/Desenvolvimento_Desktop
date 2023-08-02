lista = []
contador = 1

while contador <= 5:
    numero = int(input(f'Informe o {contador}º número da lista: '))
    lista.append(numero)
    contador += 1

print(f'Da seguinte lista informada: {lista}. O menor número é {min(lista)}, e o maior é {max(lista)}.')
