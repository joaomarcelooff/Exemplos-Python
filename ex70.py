print('-=' * 25)
print('               VAREJÃO DO VALENTINO')
print('-=' * 25)

total = 0
caros = 0
produto_mais_barato = ''
menor_preco = None  # Começa como None para detectar o primeiro produto

while True:
    produto = input('Nome do produto: ')
    valor = float(input('Preço: R$'))

    total += valor

    if valor > 1000:
        caros += 1

    # Verifica o produto mais barato
    if menor_preco is None or valor < menor_preco:
        menor_preco = valor
        produto_mais_barato = produto

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Opção inválida. Deseja continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break

print('-=' * 15)
print('FIM DO PROGRAMA'.center(40))
print('-=' * 15)
print(f'Total gasto na compra: R${total:.2f}')
print(f'Quantidade de produtos acima de R$1000: {caros}')
print(f'Produto mais barato: {produto_mais_barato} (R${menor_preco:.2f})')
