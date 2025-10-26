kg = float(input('Insira o seu peso (Kg): '))
h = float(input('Insira sua altura (m): '))
IMC = kg / h**2

print(f'O IMC dessa pessoa é de {IMC:.1f}')

if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC >= 18.5:
    print('PESO IDEAL')
elif IMC <= 30:
    print('SOBREPESO')
elif IMC <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
