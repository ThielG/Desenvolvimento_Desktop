while True:
    try:
        entrada = input('Digite um número inteiro: ')
        numero = int(entrada)
        break
    except ValueError:
        print('Entrada inválida, insira um número inteiro.')
        continue

print(f'O número digitado é {numero:.2f}.')
