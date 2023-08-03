from exercicio11 import gera_numeros_aleatorios

lista = gera_numeros_aleatorios(8)

nomes = ['Jojo', 'Josefa', 'Juju', 'Jeová']

[lista.append(nome) for nome in nomes]

dados_agrupados = ''.join([str(item) for item in lista])
print(f'Os números da lista agrupados sem espaço geram a seguinte string: {dados_agrupados}.')
