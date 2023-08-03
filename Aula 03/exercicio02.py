palavras = ('Guilherme é d4veloper e um m4l músico').split()
lista = []

for i in palavras:
    if any(c.isdigit() for c in i) == True:
        lista.append(i)

print(f'As seguintes palavras tem números entres seus caracteres: {lista}.')
