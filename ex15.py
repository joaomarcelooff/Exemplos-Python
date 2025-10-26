km = int(input('Insira a quantidade de quilometos rodados: '))
dia = int (input('Insira a quantidade de dias que o veículo foi alugado: '))
aluguel = (km * 0.15) + (dia * 60)

print (f'O total a pagar é de R${aluguel:.2f}')