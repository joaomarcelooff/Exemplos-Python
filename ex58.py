import random # Biblioteca para sortear o número
import time 
sorteio = random.randint(0, 10) # Função para computador escolher o número
 
print ('Olá, sou seu computador...')
print ('Acabei de pensar em um número entre 0 e 10')
print ('Tente adivinhar qual foi')
time.sleep(1)

print ('=' * 25)
pergunta = int(input('Insira seu palpite: '))
print ('=' * 25)

tentativas = 1 # Contador de tentativas SEMPREEEE usar no while
while pergunta != sorteio:
    if pergunta > 10:
        print ('Insira uma valor entre 0 e 10')
    elif pergunta > sorteio:
        print('Menos... Tente mais uma vez')
    else:
        print('Mais... Tente mais uma vez')
    print ('=' * 25)
    pergunta = int(input('Insira seu palpite: '))
    print ('=' * 25)
    tentativas = tentativas + 1

print(f'Acertou!!! O número era {sorteio}. Você tentou {tentativas} vezes.')