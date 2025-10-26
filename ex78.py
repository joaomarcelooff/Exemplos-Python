num = []

for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))

maior = max(num)
menor = min(num)

print(f'\nVocê digitou os valores {num}')

# Encontrando as posições do maior valor
print(f'O MAIOR valor digitado foi {maior} na(s) posição(ões): ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i} ', end='')
        
print ()

# Encontrando as posições do menor valor
print(f'O MENOR valor digitado foi {menor} na(s) posição(ões): ', end='')
for i, v in enumerate(num): #(i é a posição, v o valor)
    if v == menor:
        print(f'{i} ', end='')

