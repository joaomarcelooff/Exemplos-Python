from datetime import datetime

dados = {}

dados['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de Trabalho (Insira 0 caso não tenha): "))

if dados['ctps'] == 0:
    print("--- Dados Cadastrados ---")
    print(f" - Nome tem valor igual a {dados['nome']}")
    print(f" - Idade tem valor igual a {dados['idade']}")
    print(f" - CTPS tem valor igual a {dados['ctps']}")
    
else:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$"))

    tempo_contribuicao = datetime.now().year - dados['contratação']
    falta_contribuir = 35 - tempo_contribuicao
    dados['aposentadoria'] = dados['idade'] + falta_contribuir
    
    print("--- Dados Cadastrados ---")
    for k, v in dados.items():
        print(f' - {k} tem valor igual a {v}')