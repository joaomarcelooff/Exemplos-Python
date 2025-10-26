a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
maior = [a, b]

if a > b:
    print (f'O maior número é {a}')
elif b > a:
    print (f'O maior número é {b}')
else:
    print ('Os dois números são iguais')
    