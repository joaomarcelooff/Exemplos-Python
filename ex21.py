import pygame
import time

# Precisa inicializar o Pygame
pygame.init()

# Inicializar o áudio
pygame.mixer.init()

# Esse é para carregar o arquivo de música
pygame.mixer.music.load('Meteoro.mp3')

# Aqui vai tocar a música
pygame.mixer.music.play()

# O loop `while` mantém o programa em execução enquanto a música toca.
print("Tocando música...")
while pygame.mixer.music.get_busy():
    time.sleep(1) # pausa o script por 1 segundo para não sobrecarregar a CPU

print("Música parou.")
