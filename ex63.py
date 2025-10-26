print ('-=' * 13)
print ('  SEQUÊNCIA DE FIBONACCI')
print ('-=' * 13)

n_termos = int(input('Insira quantos termos você quer mostrar: '))

cont = 0 # Contador obrigatorio para usar o while
termo1 = 0
termo2 = 1

while cont <= n_termos:
    print(f'{termo1} → ', end='')
    proximo = termo1 + termo2
    termo1 = termo2 # Aqui acontece o loop necessário!
    termo2 = proximo
    cont = cont + 1
print ('FIM')