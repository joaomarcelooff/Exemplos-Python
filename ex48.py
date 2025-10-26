soma = 0 # ACUMULADOR
for n_impares in range (1, 501, 2): # Aqui ja vai pegar todos os impares
    if n_impares % 3 == 0: # Aqui vai selecionar apenas os multiplos de 3
        soma = soma + n_impares
print (f'A soma de todos os numeros impares e múltiplos de três no intervalo de [1 - 500] é de: {soma}')

