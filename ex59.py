import time
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

opção = 0  # Inicializa a variável para entrar no while

while opção != 5:
    print('\n[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR NÚMERO')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')

    opção = int(input('>>>>> Insira sua opção: '))
    time.sleep(1)

    if opção == 1:
        print(f'A soma entre {a} + {b} é {a + b}')
    elif opção == 2:
        print(f'O resultado de {a} x {b} é {a * b}')
    elif opção == 3:
        print(f'Entre {a} e {b}, o maior valor é {max(a, b)}')
    elif opção == 4:
        a = int(input('Novo primeiro valor: '))
        b = int(input('Novo segundo valor: '))
    elif opção == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida! Tente novamente.')

print('Programa encerrado. Volte sempre!')