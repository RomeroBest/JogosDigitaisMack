import pygame
import random

def create_rectangle(width, height, color, position):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surface, color, (0, 0, width, height))
    rect = surface.get_rect()
    rect.topleft = position
    return surface, rect

def create_circle(radius, color, position):   
    diameter = radius * 2
    surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (radius, radius), radius)
    rect = surface.get_rect()
    rect.topleft = position
    return surface, rect

def random_color():
    """
    Retorna uma tupla representando uma cor RGB com valores aleatórios
    entre 0 e 255 para cada canal (red, green e blue).
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Exemplo de uso:
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Criando formas com cores aleatórias
rect_surface, rect_rect = create_rectangle(100, 50, random_color(), (100, 100))
circle_surface, circle_rect = create_circle(30, random_color(), (300, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fundo branco
    
    # Desenhando as formas
    screen.blit(rect_surface, rect_rect)
    screen.blit(circle_surface, circle_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()