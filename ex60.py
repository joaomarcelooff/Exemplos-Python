num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
contador = num

print(f'\nCalculando {num}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(f'{fatorial}')
