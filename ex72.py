numeros = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {numeros[escolha]}')
        break
    else:
        print('Valor inválido. Por favor, digite um número entre 0 e 20.')
