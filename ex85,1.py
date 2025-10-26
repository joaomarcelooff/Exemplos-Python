# Programa utilizando duas listas em uma
lista_num = [[], []]
num = 0

for i in range (1,8):
    num = int(input(f'Insira o {i}o. valor: '))
    
    if num % 2 ==0:
        lista_num[0].append(num)
    else:
        lista_num[1].append(num)
        
lista_num[0].sort()
lista_num[1].sort()

print (f'Os valores digitados foram {num[0]}')
print (f'Os valores ímpares digitados foram {num[1]}')