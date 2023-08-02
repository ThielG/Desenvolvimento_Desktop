palavra = input('Informe uma palavra: ').lower()
inverso = palavra[::-1]

if palavra == inverso:
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')
