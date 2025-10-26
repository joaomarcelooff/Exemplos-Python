lista_num = []
num_pares = []
num_impares = []

while True:
    num = int(input('Digite um valor: '))
    
    if num in lista_num:
        print ('Número já foi inserido anteriormente!')
        
    else:
        lista_num.append(num)
        if num % 2 == 0:
            num_pares.append(num)
        elif num % 2 != 0:
            num_impares.append(num)
     
    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')
    
    if pergunta == 'N':
        break
    

print ()
print (f'A lista completa é {lista_num}')
print (f'A lista de números pares é {num_pares}')
print (f'A lista de números ímpares é {num_impares}')
        