while True:
    print('=' * 50)
    num = int(input('Insira o valor para ter acesso à sua tabuada: '))
    print('=' * 50)

    if num < 0:
        print('Programa encerrado. Obrigado!')
        break

    for i in range(1, 11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')

    
        