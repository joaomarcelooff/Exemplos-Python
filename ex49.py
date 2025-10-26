# Solicita um número ao usuário
num = int(input('Digite um número para ver a tabuada: '))

# Laço for para multiplicar de 1 a 10
print(f'\033[1m=====Tabuada do {num}====\033[0m')
for i in range(1, 11):  # range(1, 11) vai de 1 até 10
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
