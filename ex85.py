lista_num = []
num_impares = []

for i in range (1,8):
    num = int(input(f'Insira o {i}o. valor: '))
    lista_num.append(num)
    
    if num % 2 !=0:
        num_impares.append(num)
        

print (f'Os valores digitados foram {lista_num}')
print (f'Os valores ímpares digitados foram {num_impares}')
print ("Obrigado por utilizar nosso programa!")