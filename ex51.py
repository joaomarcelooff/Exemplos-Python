print ('=' * 35)
print ('        10 TERMOS DE UMA PA   ')
print ('=' * 35)


primeiro_termo = int(input('Insira o valor do primeiro termo: '))
razão = int(input('Insira o valor da razão da PA: '))
n_termo = primeiro_termo + (10 - 1) * razão # Fórmula matemática para encontrar o n termo

for n in range (primeiro_termo, n_termo, razão):
    print (n, end= ' -> ' )
print ('ACABOU!')
