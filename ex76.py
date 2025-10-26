# COMO COLOCAR VARIAS INFORMAÇÕES DENTRO DE UMA TUPLA !!!!

listagem = ('Lápis', '1.50'
            'Borracha', '0.5'
            'Caderno', '16'
            'Estojo', '5')

print ('-' * 40)
print (f'{"PAPELARIA VALENTINO":^40}')
print ('-' * 40)

for posição in range (0, len(listagem)):
    if posição % 2 == 0:
        print (f'{listagem[posição]:.<30}', end = '')
    else:
        print (f'R${listagem[posição]:>7.2f}')
        