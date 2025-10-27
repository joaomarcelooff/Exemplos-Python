import random
from time import sleep
import operator

pessoas = {'jogadores' : ['Silky', 'Jujube', 'Trinity', 'Sasha']}
resultados = {} # Aqui vão ser armazenados os resultados do dado de cada um

for nome in pessoas['jogadores']:
    numero_sorteado = random.randint(1, 6)
    resultados[nome] = numero_sorteado

print("Valores sorteados: ")
for nome, numero in resultados.items():
    print (f'- Jogador {nome} tirou {numero} no dado')
    sleep(1)
    
ranking = sorted(resultados.items(), key = operator.itemgetter(1), reverse = True)

print('<<< RANKING DE JOGADORES >>>')
sleep(1)

# 'posicao' é a variável que vai contar a posição no ranking (1º, 2º, etc.)
posicao = 1 

# O 'ranking' é uma lista de tuplas, onde cada tupla é (nome, número)
for jogador, ponto in ranking:
    print(f' {posicao}º lugar: {jogador} com {ponto} pontos.')
    posicao += 1
    sleep(1)