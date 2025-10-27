# ESSE CODIGO É O DO EXEMPLO 90, SO QUE MELHORADO!
escola = {}

escola ['nome'] = str(input("Nome: "))
escola ['media'] = float(input("Media do aluno: "))

if escola['media'] >= 7:
    escola['situação'] = 'Aprovado'
    
elif escola['media'] < 7:
    escola['situação'] = 'Recuperação'

else:
    escola['situação'] = 'Reprovado'
    
print ('-=' * 25)
for k, v in escola.items():
    print(f' - {k} é igual a {v}')