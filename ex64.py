n = int(input('Digite um número (999 para parar): '))

cont = 0
soma = 0
while True:
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
    
print (f'Você digitou {cont} números e a soma entre eles foi {soma}')
