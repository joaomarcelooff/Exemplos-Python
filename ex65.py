lista_numeros = []
cont = 0
soma = 0

while True:
    num = int(input('Digite um número: '))
    lista_numeros.append(num)
    cont = cont + 1
    soma = soma + num
    
    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')
    
    if pergunta == 'N':
        break

media = soma / cont
maior_num = max(lista_numeros)
menor_num = min(lista_numeros)
print (f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior_num} e o menor foi {menor_num}')
