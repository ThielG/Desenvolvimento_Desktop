def verifica_numero_par(numero):

    if isinstance(numero, int) == True:
        print(f'O número digitado é inteiro.')
        if numero % 2 == 0:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')
    else:
        print('Não é um número inteiro.')

    return

numero = verifica_numero_par(int(input('Informe um número: ')))
