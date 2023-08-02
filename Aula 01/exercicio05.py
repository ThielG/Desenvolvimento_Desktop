turmas = int(input('Informe a quantidade de turmas: '))
lista = []
contador = 1
media = 0

while contador <= turmas:
    alunos = int(input(f'Informe a quantidade de alunos da {contador}° turma: '))
    if alunos > 40:
        print('A turma não pode ter mais de 40 alunos, informe novamente!')
        continue
    lista.append(alunos)
    contador += 1

print(f'\nA média de alunos por turma é: {round(sum(lista) / turmas)}.')
