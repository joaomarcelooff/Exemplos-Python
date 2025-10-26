soma = 0
cont = 0

for num in range(1, 7):
    num = int(input(f'Insira o {num}° valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
    
print (f'Você informou {cont} números PARES e a soma dos valores pares é igual à {soma}')