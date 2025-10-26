import random

numeros = []

# PRESTAR ATENÇÃO NA LÓGICA !!!
while len(numeros) < 5:
    n = random.randint(1, 10)
    if n not in numeros:
        numeros.append(n)

print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')