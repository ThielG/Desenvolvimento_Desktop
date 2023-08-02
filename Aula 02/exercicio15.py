frutas = {
     'Maças': 2,
     'Melão': 1,
     'Tangerinas': 6,
     'Wikis': 4,
     'Melancia': 1
}

print('Fruta'.ljust(12), 'Quantidade')
print('-----------------------')

for fruta, quantidade in frutas.items():
    print(fruta.ljust(12), quantidade)
