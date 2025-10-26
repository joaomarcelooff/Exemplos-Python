print('-=' * 11)
print(' CADASTRE UMA PESSOA')
print('-=' * 11)

cont = 0
homens = 0
mulheres = 0
maior_idade = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [F/M] ').strip().upper()
    
    if sexo not in ['M', 'F']:
        print('Sexo inválido. Por favor, digite F ou M.')
        continue  # volta ao início do while
    
    # Contador geral
    cont += 1

    # Contador por sexo
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1

    # Contador de maiores de idade
    if idade > 18:
        maior_idade += 1

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 11)
print(f'O total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s)')
print(f'E temos {mulheres} mulher(es) cadastrada(s)')
