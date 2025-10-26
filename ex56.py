anos = [] # Lista das idades para fazer uma média
idade_H = [] # Lista das idade dos homens
nome_H_velho = '' # Nome do homem mais velho
idade_H_velho = 0 # Idade do homem mais velho
M_novas = 0 # Quantidade de mulheres com menos de 20 anos

for i in range (1, 5):
    print (f'====== {i} PESSOA ======')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
      
    anos.append(idade)
    media_idade = sum(anos) / 4 # Função 'sum' serve para somar itens de uma lista
    
    if sexo == 'M': # Como é uma str precisa estar entre aspas
        idade_H.append(idade)

        if idade > idade_H_velho: # Esse IF vai definir a idade e o nome do homem mais velho
            idade_H_velho = idade
            nome_H_velho = nome
            
    if sexo == 'F' and idade < 20:
                M_novas += 1

print (f'A média de idade do grupo é de {media_idade:.1f} anos')

if idade_H:
    print(f'O homem mais velho tem {idade_H_velho} anos e se chama {nome_H_velho}.')
else:
    print('Não há homens no grupo.')
    
print (f'Ao todo são {M_novas} mulheres com menos de 20 anos')