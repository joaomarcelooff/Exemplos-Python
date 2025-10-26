lista_num = []

while True:
    num = int(input('Digite um valor: '))
    
    if num in lista_num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista_num.append(num)
        print('Número adicionado com sucesso...')
    
    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')
    
    if pergunta == 'N':
        break

print ()
print (f'Você digitou {len(lista_num)} elementos')

lista_num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista_num}')

if 5 in lista_num:
    print (f'O valor 5 foi encontrado na lista')
else:
    print ('O valor 5 não foi encontrado na lista')