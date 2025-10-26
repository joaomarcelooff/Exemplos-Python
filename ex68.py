import random

vitorias = 0  # CONTADOR DE VITÓRIAS

while True:
    print('-=' * 18)
    print('      VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 18)
    
    # INFORMAÇÕES DE ENTRADA
    user = int(input('Digite um valor: '))
    choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    comp = random.randint(1, 10)
    soma = user + comp

    # CONDIÇÃO DE PAR OU ÍMPAR
    if soma % 2 == 0:
        resultado = 'DEU PAR'
    else:
        resultado = 'DEU ÍMPAR'
    
    # EXIBIÇÃO DO RESULTADO FINAL
    print('-' * 50)
    print(f'Você jogou {user} e o computador {comp}. O total foi {soma}. {resultado}')
    print('-' * 50)

    # VERIFICAÇÃO DE DERROTA OU VITÓRIA
    if (choice == 'I' and resultado == 'DEU PAR') or (choice == 'P' and resultado == 'DEU ÍMPAR'):
        print('GAME OVER')
        print(f'Você venceu {vitorias} vez(es) antes de perder.')
        break
    else:
        print('Você VENCEU!\nVamos jogar novamente...\n')
        vitorias += 1  