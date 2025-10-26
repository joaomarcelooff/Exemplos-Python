quilos = []

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    quilos.append(peso)

maior_peso = max(quilos)
menor_peso = min(quilos)

print(f'\nO MAIOR peso lido foi de {maior_peso:.1f}Kg')
print(f'O MENOR peso lido foi de {menor_peso:.1f}Kg')
