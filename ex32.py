ano = int(input('Insira um ano para descobrir se ele é bissexto: '))

if (ano % 4 == 0 and ano % 100) or (ano % 400 == 0):
    print (f'{ano} É BISSEXTO!')
else:
    print (f'{ano} NÃO É BISSEXTO!')
    