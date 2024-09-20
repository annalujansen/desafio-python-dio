entrada = '''
Digite as letra D, S, E e q para cada operação desejada:

[D]epósito
[S]aque
[E]xtrato
[0]-Sair

'''
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    operacao = input(entrada)

    if operacao == '0':
        break

    elif operacao == 'D':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('O valor informado é inválido.')

    elif operacao == 'S':
        valor = float(input('Informe o valor de saque: '))

        if valor > saldo:
            print('Operação inválida. Excedeu o saldo.')

        elif valor > 500:
            print('Operação inválida. O limite de saque é de R$ 500,00.')

        elif numero_saques >= LIMITE_SAQUES:
            print('Operação inválida. Limite de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques+=1

        else:
            ('O valor informado é inválido.')

    elif operacao == 'E':
        texto = 'EXTRATO'
        print(f'{texto:=^27}\n')
        print(extrato if extrato else f'{"Não hoDuve operações": ^27}\n')
        print(f'Saldo: R${saldo:.2f}\n')
        print('='*27)

    else:
        print('A operação escolhida é inválida, por favor selecione novamente a operação desejada.')
