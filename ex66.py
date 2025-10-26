soma = 0
cont = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))  # Corrigido aqui
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} valores foi {soma}')
