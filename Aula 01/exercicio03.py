lista = []
consoantes = []
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

while contador < 10:
    caracteres = input('Informe dez caracteres: ').lower()
    contador += 1
    lista.append(caracteres)
    if caracteres not in vogais:
        consoantes.append(caracteres)

print(f'\nDos seguintes caracteres digitados: {lista}.\nApenas esses são consoantes: {consoantes}.'
      f'\nNota-se um total de: {len(consoantes)} consoantes.')
