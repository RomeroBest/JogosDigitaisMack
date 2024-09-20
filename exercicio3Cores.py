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
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_position(max_x, max_y):
    return (random.randint(0, max_x), random.randint(0, max_y))

def random_size(min_size, max_size):
    return random.randint(min_size, max_size)

# Inicialização do Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Formas Geométricas Aleatórias")
clock = pygame.time.Clock()

# Lista para armazenar as formas
shapes = []

# Gerar formas aleatórias
num_shapes = 20
for _ in range(num_shapes):
    if random.choice([True, False]):  # 50% de chance para retângulo ou círculo
        w = random_size(20, 100)
        h = random_size(20, 100)
        rect_surface, rect_rect = create_rectangle(w, h, random_color(), random_position(width - w, height - h))
        shapes.append((rect_surface, rect_rect))
    else:
        r = random_size(10, 50)
        circle_surface, circle_rect = create_circle(r, random_color(), random_position(width - 2*r, height - 2*r))
        shapes.append((circle_surface, circle_rect))

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Regerar formas quando a barra de espaço é pressionada
                shapes.clear()
                for _ in range(num_shapes):
                    if random.choice([True, False]):
                        w = random_size(20, 100)
                        h = random_size(20, 100)
                        rect_surface, rect_rect = create_rectangle(w, h, random_color(), random_position(width - w, height - h))
                        shapes.append((rect_surface, rect_rect))
                    else:
                        r = random_size(10, 50)
                        circle_surface, circle_rect = create_circle(r, random_color(), random_position(width - 2*r, height - 2*r))
                        shapes.append((circle_surface, circle_rect))

    # Limpar a tela
    screen.fill((255, 255, 255))  # Fundo branco
    
    # Desenhar todas as formas
    for shape_surface, shape_rect in shapes:
        screen.blit(shape_surface, shape_rect)

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()