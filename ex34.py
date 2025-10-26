sal = float(input('Insira o valor do seu salário e descubra o valor do seu aumento: '))

if sal > 1250.00:
    aumento = sal * 1.10  # 10% de aumento
else:
    aumento = sal * 1.15  # 15% de aumento

print(f'Seu novo salário é R${aumento:.2f}')