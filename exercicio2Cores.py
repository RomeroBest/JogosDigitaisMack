import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Transição de Cores Aleatórias")

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

# Função para gerar uma cor aleatória
def generate_random_color():
    """Gera uma tupla de cor RGB com valores aleatórios entre 0 e 255."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Função para interpolação linear
def lerp(value1, value2, factor):
    return int(value1 + (value2 - value1) * factor)

# Inicializa as cores
current_color_rect = generate_random_color()
current_color_circle = generate_random_color()
target_color_rect = generate_random_color()
target_color_circle = generate_random_color()
transition_speed = 0.01  # Velocidade de transição
alpha = 0.0  # Fator de transição

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a cor com interpolação
    if alpha < 1.0:
        current_color_rect = (
            lerp(current_color_rect[0], target_color_rect[0], alpha),
            lerp(current_color_rect[1], target_color_rect[1], alpha),
            lerp(current_color_rect[2], target_color_rect[2], alpha)
        )
        
        current_color_circle = (
            lerp(current_color_circle[0], target_color_circle[0], alpha),
            lerp(current_color_circle[1], target_color_circle[1], alpha),
            lerp(current_color_circle[2], target_color_circle[2], alpha)
        )
        
        alpha += transition_speed
    else:
        # Troca as cores alvo quando a transição terminar
        target_color_rect = generate_random_color()
        target_color_circle = generate_random_color()
        alpha = 0.0  # Reinicia o fator de transição

    # Preenche o fundo
    screen.fill((255, 255, 255))  # Fundo branco

    # Cria e desenha um retângulo com a cor atual
    rect_surface, rect_position = create_rectangle(200, 100, current_color_rect, (100, 100))
    screen.blit(rect_surface, rect_position)

    # Cria e desenha um círculo com a cor atual
    circle_surface, circle_position = create_circle(50, current_color_circle, (400, 300))
    screen.blit(circle_surface, circle_position)

    # Atualiza a tela
    pygame.display.flip()