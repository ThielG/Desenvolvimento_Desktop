primeiro = input('Informe a primeira string: ')
segundo = input('Informe a segunda string: ')

len_primeiro = len(primeiro)
len_segundo = len(segundo)

print(f'A primeira string "{primeiro}" tem um total de: {len_primeiro} caracteres.\nA segunda string "{segundo}" tem um total de: {len_segundo} caracteres.')

if len_primeiro == len_segundo:
    print('\nAs duas palavras tem o mesmo comprimento!')
else:
    print('\nAs duas palavras não tem o mesmo comprimento!')
