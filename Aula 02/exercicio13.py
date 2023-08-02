primeiro = 0
segundo = 1
lista = [0, 1]
contador = 1

while contador < 13:
    primeiro += segundo
    lista.append(primeiro)
    contador += 1
    segundo += primeiro
    lista.append(segundo)
    contador += 1

print(lista)
