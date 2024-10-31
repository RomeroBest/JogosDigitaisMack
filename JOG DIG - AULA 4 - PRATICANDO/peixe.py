import pygame
from pygame.locals import *
from sys import exit
from pygame.math import Vector2

# Carregando arquivos
background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

# Inicializando o Pygame
pygame.init()

# Configurando a tela
screen = pygame.display.set_mode((640, 480), 0, 32)

# Carregando imagens
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

# Inicializando o relógio
clock = pygame.time.Clock()

# Definindo posição e direção iniciais como objetos Vector2
position = Vector2(100, 200)
heading = Vector2(1, 0.5).normalize()  # Direção inicial (diagonal)
speed = 250  # Velocidade do peixe

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movendo o sprite na direção do heading
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    position += heading * distance_moved

    # Checando colisão com as bordas da tela e invertendo a direção
    if position.x <= 0 or position.x + sprite.get_width() >= 640:
        heading.x = -heading.x  # Inverte a direção horizontal
    if position.y <= 0 or position.y + sprite.get_height() >= 480:
        heading.y = -heading.y  # Inverte a direção vertical

    # Desenhando o fundo e o sprite
    screen.blit(background, (0, 0))
    screen.blit(sprite, (position.x, position.y))

    # Atualizando a tela
    pygame.display.update()
