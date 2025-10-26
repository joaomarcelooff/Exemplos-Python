from datetime import date

maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for pergunta_idade in range (1, 8):
    ano = int(input(f'Insira o ano de nascimento da {pergunta_idade}° pessoa: '))
    if ano_atual - ano >= 18:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1

print (f'Ao todo tivemos {maior_idade} pessoas MAIORES DE IDADE\nE também {menor_idade} pessoas MENORES DE IDADE')