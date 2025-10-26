from datetime import date
atual = date.today().year # Usado para que o programa possa ser util em qualquer ano
                          # Porque se eu usar 2025 vai estar limitado apenas para esse ano
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano
print (f'O atleta tem {idade} anos')

if idade <= 9:
    print ('Classificação do atleta: MIRIM')
elif idade <= 14:
    print ('Classificação do atleta: INFANTIL')
elif idade <= 19:
    print ('Classificação do atleta: JUNIOR')
elif idade <= 25:
    print ('Classificação do atleta: SÊNIOR')
else:
    print ('Classificação do atleta: MASTER')
    