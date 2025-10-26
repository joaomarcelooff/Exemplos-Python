from colorama import Fore, Style  # Biblioteca de cores nos textos

num = int(input('Digite um número: '))
q_primo = 0  # Contador de números primos

for primo in range(1, num + 1):
    if num % primo == 0:
        q_primo = q_primo + 1
        print(Fore.RED + str(primo), end=' ' + Style.RESET_ALL)  # Vermelho para divisores
    else:
        print(Fore.WHITE + str(primo), end=' ' + Style.RESET_ALL)  # Branco para não divisores

print(f'\nO número {num} foi divisível {q_primo} vezes')
if q_primo > 2:
    print(f'Portanto, {num} NÃO é primo')
else:
    print(f'Portanto, {num} é primo')
