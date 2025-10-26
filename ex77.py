palavras = ['APRENDER', 'PROGRAMAR', 'PYTHON', 'ESTUDAR']
vogais = 'AEIOU'  # Pode ser string, já que vamos verificar letra por letra

for palavra in palavras:
    print(f'Na palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=' ')
    print()  # Para pular de linha depois de cada palavra
