print('=' * 15)
print(' GERADOR DE PA')
print('=' * 15)

primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

termo = primeiro_termo
cont = 1
total = 0
mais = 10  # Começamos com 10 termos

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {total} termos mostrados.')
