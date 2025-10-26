import random
print ('Suas opções:')
print ('PEDRA \nPAPEL \nTESOURA')

user = str(input('Insira sua opção: ')) # Escolha do jogador

palavras = ['PEDRA', 'PAPEL', 'TESOURA']
comp = random.choice(palavras) # Escolha do computador

print ('-=' * 13)
print (f'Computador jogou {comp}')
print (f'Usuário jogou {user}')
print ('-=' * 13)

if user == 'PEDRA' and comp == 'PEDRA' or user == 'PAPEL' and comp == 'PAPEL' or user == 'TESOURA' and comp == 'TESOURA': # casos de empate
    print ('EMPATE!!!') 

elif user == 'PEDRA' and comp == 'TESOURA' or user == 'PAPEL' and comp == 'PEDRA' or user == 'TESOURA' and comp == 'PAPEL': # casos que o usuario ganha
    print ('USUÁRIO VENCEU!!!')

elif user == 'PEDRA' and comp == 'PAPEL' or user == 'PAPEL' and comp == 'TESOURA' or user == 'TESOURA' and comp == 'PEDRA': # casos que o computador ganha
    print ('CPU VENCEU!!!')
