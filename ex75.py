a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

lista = [a, b, c, d]

print ('-=' * 20)
print (f'Você digitou os valores {lista}')

# CONTANDO QUANTAS VEZES O 9 APARECE
qnt_9 = 0
qnt_9 = lista.count(9)
print(f'O valor 9 foi digitado {qnt_9} vez(es)')

# CONTANDO QUANTAS NÚMEROS PARES APARECE
qtd_pares = 0
for num in lista:
    if num % 2 == 0:
        qtd_pares += 1

print(f'Tiveram {qtd_pares} número(s) par(es)')

# EM QUE POSIÇÃO FICOU O VALOR 3
if 3 in lista:
    posicao = lista.index(3)
    print(f'O número 3 foi digitado e está na posição {posicao}')
else:
    print('O número 3 não foi digitado.')
    
print('-=' * 20)