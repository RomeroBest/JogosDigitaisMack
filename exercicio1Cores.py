import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Exemplo de Geometrias")

# Função para criar um retângulo
def create_rectangle(width, height, color, position):
    rect_surface = pygame.Surface((width, height))
    rect_surface.fill(color)
    return rect_surface, position

# Função para criar um círculo
def create_circle(radius, color, position):
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, color, (radius, radius), radius)
    return circle_surface, position

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche o fundo
    screen.fill(WHITE)

    # Cria e desenha um retângulo
    rect_surface, rect_position = create_rectangle(200, 100, BLUE, (100, 100))
    screen.blit(rect_surface, rect_position)

    # Cria e desenha um círculo
    circle_surface, circle_position = create_circle(50, RED, (400, 300))
    screen.blit(circle_surface, circle_position)

    # Atualiza a tela
    pygame.display.flip()