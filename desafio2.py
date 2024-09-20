import pygame

def lerp(start, end, t):
    return start + (end - start) * t

def lerp_color(color1, color2, t):
    return tuple(int(lerp(c1, c2, t)) for c1, c2 in zip(color1, color2))

# Inicialização do Pygame
pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retângulos Interativos com Cores Persistentes")
clock = pygame.time.Clock()

# Configuração dos retângulos
num_rectangles = 6
rectangle_width = width // 3
rectangle_height = height // 2
rectangles = []

for i in range(num_rectangles):
    x = (i % 3) * rectangle_width
    y = (i // 3) * rectangle_height
    rectangles.append({
        'rect': pygame.Rect(x, y, rectangle_width, rectangle_height),
        'color': (128, 128, 128),  # Cor inicial cinza
        'last_color': None,  # Última cor quando o mouse estava sobre o retângulo
        'hover': False  # Flag para indicar se o mouse está sobre o retângulo
    })

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            for rect in rectangles:
                if rect['rect'].collidepoint(mouse_pos):
                    if not rect['hover']:
                        rect['hover'] = True
                        # Calcula a nova cor apenas quando o mouse entra no retângulo
                        rel_x = (mouse_pos[0] - rect['rect'].left) / rect['rect'].width
                        rel_y = (mouse_pos[1] - rect['rect'].top) / rect['rect'].height
                        red_to_green = lerp_color((255, 0, 0), (0, 255, 0), rel_x)
                        new_color = lerp_color(red_to_green, (0, 0, 255), rel_y)
                        rect['last_color'] = new_color
                        rect['color'] = new_color
                else:
                    rect['hover'] = False
                    if rect['last_color']:
                        rect['color'] = rect['last_color']

    # Desenhar retângulos
    for rect in rectangles:
        pygame.draw.rect(screen, rect['color'], rect['rect'])

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()