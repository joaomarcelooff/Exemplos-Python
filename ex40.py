import statistics

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = statistics.mean([n1, n2]) # Os valores precisam estar entre colchetes
print(f'Média: {media:.1f}')

if media < 5.0:
    print ('Aluno\033[31m REPROVADO')
    
elif media >= 5 and media <= 6.9:
    print ('Aluno de\033[33m RECUPERAÇÃO')
    
else:
    print ('Aluno\033[32m APROVADO')
