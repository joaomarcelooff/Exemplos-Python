print('======= LOJAS VALENTINO =======')
preço = float(input('Preço das compras: R$'))

print('\nFORMAS DE PAGAMENTO')
print('[ 1 ] À vista/cheque (10% de desconto)')
print('[ 2 ] À vista no cartão (5% de desconto)')
print('[ 3 ] 2x no cartão (preço normal)')
print('[ 4 ] 3x ou mais no cartão (20% de juros)')

opção = int(input('\nInsira sua opção de pagamento: '))

if opção == 1:
    total = preço * 0.90
    print(f'\nSua compra de R${preço:.2f} vai custar R${total:.2f} com 10% de desconto.')

elif opção == 2:
    total = preço * 0.95
    print(f'\nSua compra de R${preço:.2f} vai custar R${total:.2f} com 5% de desconto.')

elif opção == 3:
    parcela = preço / 2
    print(f'\nSua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
    print(f'Total da compra: R${preço:.2f}')

elif opção == 4:
    n_parcelas = int(input('Insira a quantidade de parcelas (3 ou mais): '))
    if n_parcelas < 3:
        print('Número de parcelas inválido para essa opção.')
    else:
        total = preço * 1.20
        parcela = total / n_parcelas
        print(f'\nSua compra será parcelada em {n_parcelas}x de R${parcela:.2f} COM JUROS.')
        print(f'Total da compra: R${total:.2f}')
else:
    print('\nOpção inválida. Tente novamente.')
