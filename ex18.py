# Usar a funcionalidade random
import random

a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))
# Agora vou criar a lista para incluir todos esses nomes
lista = [a, b, c, d]

#shufle vai embaralhar os nomes aleatoriamente
random.shuffle(lista)
print (f'O nome escolhido foi {lista}')