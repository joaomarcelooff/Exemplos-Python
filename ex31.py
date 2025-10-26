km = int(input('Insira a distância percorrida em km durante sua viajem: '))

if km <= 200:
    preco = km * 0.5
    print (f'O preço da sua passagem é de R${preco}')
elif km > 200: # Else NÃO pode ter condição, então usa-se o ELIF
    preco = km * 0.45
    print (f'O preço da sua passagem é de R${preco}')