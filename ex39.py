from datetime import date
atual = date.today().year # Usado para que o programa possa ser util em qualquer ano
                          # Porque se eu usar 2025 vai estar limitado apenas para esse ano
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano

print (f'Quem nasceu em {ano} tem {idade} anos em {atual}')

if idade > 18:
    print (f'Você já deveria ter se alistado há {idade - 18} anos')
    print (f'Seu alistamento foi em {ano + 18}')
elif idade < 18:
    print (f'Ainda faltam {18 - idade} ano(s) para o alistamento')
    print (f'Seu alistamento será em {ano + 18}')
    
elif idade == 18:
    print (f'Você tem que se alistar imediatamente')