print ('=' * 15)
print (' GERADOR DE PA')
print ('=' * 15)

primeiro_termo = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))

cont = 1
termo = primeiro_termo

while cont <= 10:
    print (f'{termo} -> ' , end= '')
    termo = termo + razão
    cont = cont + 1
print ('FIM')