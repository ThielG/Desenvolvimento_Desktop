primeira = float(input('Informe a primeira nota: '))
segunda = float(input('Informe a segunda nota: '))
terceira = float(input('Informe a terceira nota: '))
quarta = float(input('Informe a quarta nota: '))

notas = [primeira, segunda, terceira, quarta]
media = (sum(notas) / 4)

print('\nAvaliação | Nota')
print('----------------')

for i in range(len(notas)):
    print(f'{(i + 1):8}° | {notas[i]:4}')

print('----------------')
print(f'Média:      {round(media, 2)}')
print('----------------')

if media >= 7.0:
    print(f'\nParabéns, você foi aprovado!')
elif media < 7.0:
    print(f'\nInfelizmente você ficou de recuperação.')
    recuperacao = float(input('\nInforme a nota da prova final: '))
    notas.append(recuperacao)
    final = round(sum(notas) / 5, 2)
    print(final)
    if final >= 5:
        print('Aprovado!')
    else:
        print('Reprovado.')
