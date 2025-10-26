casa = float(input('Insira o valor do imóvel: '))
salario = float(input('Insira o valor do seu salário: '))
parcelas = int(input('Insira em quantos anos desena pagar esse imóvel: '))
               

prestação = casa / (parcelas * 12)
print(f'Para pagar uma casa de R${casa} em {parcelas} anos a prestação será de R${prestação:.2f}')


if prestação > (salario * 30) / 100:
    print('MPREPRÉSTIMO NEGADO!!!')
else:
    print('EMPRESTIMO APROVADO!!!')