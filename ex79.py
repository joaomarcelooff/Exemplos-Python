lista_numeros = []

while True:
    num = int(input('Digite um número: '))
    
    if num in lista_numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista_numeros.append(num)
        print('Número adicionado com sucesso...')
    
    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')
    
    if pergunta == 'N':
        break
    
print('-=' * 30)
print(f'Você digitou os valores {lista_numeros}')    