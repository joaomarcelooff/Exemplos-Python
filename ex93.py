jogador = {}
lista_gols = []
total = 0

jogador['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Insira quantas partidas o {jogador['nome']} jogou: "))
jogador['partidas'] = partidas

print('-=' * 25)

if partidas < 1: 
    print(f"O jogador {jogador['nome']} não jogou nenhuma partida")
    
else:
    for i in range (0, jogador['partidas']):
        gols = int(input(f"Insira quantos gols fez na {i + 1} partida: ")) # Precisa criar uma lista para armazenar os gols
        lista_gols.append(gols)
        total = total + gols
        
jogador['gols'] = lista_gols
jogador['total_gols'] = total       

print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
        print(f' - O campo {k} tem valor igual a {v}')
        
print('-=' *25)
print(f"O jogador {jogador['nome']} jogou {partidas}.")
for j in range (0, jogador['partidas']):
    gol_da_partida = lista_gols[j] 
    
    print(f"=> Na partida {j + 1}, fez {gol_da_partida} gols")

print(f"Foi um total de {jogador['total_gols']} gols.")