import pygame
import random

def lerp(start, end, t):
    return start + (end - start) * t

def lerp_color(color1, color2, t):
    return tuple(lerp(c1, c2, t) for c1, c2 in zip(color1, color2))

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Inicialização do Pygame
pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retângulos com Cores em Transição")
clock = pygame.time.Clock()

# Configuração dos retângulos
num_rectangles = 6
rectangle_width = width // 3
rectangle_height = height // 2
rectangles = []

for i in range(num_rectangles):
    x = (i % 3) * rectangle_width
    y = (i // 3) * rectangle_height
    start_color = random_color()
    end_color = random_color()
    rectangles.append({
        'rect': pygame.Rect(x, y, rectangle_width, rectangle_height),
        'start_color': start_color,
        'end_color': end_color,
        't': 0,
        'direction': 1
    })

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar cores
    for rect in rectangles:
        rect['t'] += 0.01 * rect['direction']
        if rect['t'] >= 1 or rect['t'] <= 0:
            rect['direction'] *= -1
            if rect['t'] >= 1:
                rect['start_color'] = rect['end_color']
                rect['end_color'] = random_color()
            rect['t'] = max(0, min(1, rect['t']))  # Garante que t fique entre 0 e 1

    # Desenhar retângulos
    for rect in rectangles:
        color = lerp_color(rect['start_color'], rect['end_color'], rect['t'])
        pygame.draw.rect(screen, color, rect['rect'])

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()