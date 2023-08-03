lista = ['Emanuela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']
lista = list(filter(None, lista))

print(lista)

# Como o profesor fez:

lista_nomes = ['Emanuela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']
lista_nomes = [nome for nome in lista_nomes if nome and nome.strip()]

print(f'Os itens de lista que não estão em branco ou nulo são: {lista_nomes}.')
