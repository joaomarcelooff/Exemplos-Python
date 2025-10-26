a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))

if (a > b) and (a > c) and (b > c): 
    print(f'O maior valor é {a} e o menor valor é {c}')
elif (a > b) and (a > c) and (c > b):
    print(f'O maior valor é {a} e o menor valor é {b}')
elif (b > a) and (b > c) and (a > c):
    print(f'O maior valor é {b} e o menor valor é {c}')
elif (b > a) and (b > c) and (c > a):
    print(f'O maior valor é {b} e o menor valor é {a}')
elif (c > a) and (c > b) and (a > b):
    print(f'O maior valor é {c} e o menor valor é {b}')
elif (c > a) and (c > b) and (b > a):
    print(f'O maior valor é {c} e o menor valor é {a}')

# Uma forma mais facil de fazer isso é usando a função MAX E MIM do python
# a = int(input('Insira o primeiro valor: '))
# b = int(input('Insira o segundo valor: '))
# c = int(input('Insira o terceiro valor: '))

# maior = max(a, b, c)
# menor = min(a, b, c)

# print(f'O maior valor é {maior} e o menor valor é {menor}')