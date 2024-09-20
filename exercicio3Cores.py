import pygame
import random

# Constantes
WIDTH, HEIGHT = 800, 600
NUM_SHAPES = 20
MIN_SIZE = 20
MAX_SIZE = 100
MIN_RADIUS = 10
MAX_RADIUS = 50

# Cores
WHITE = (255, 255, 255)

def create_rectangle(width, height, color, position):
    #Cria um retângulo com a largura, altura, cor e posição especificadas
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surface, color, (0, 0, width, height))
    rect = surface.get_rect()
    rect.topleft = position
    return surface, rect

def create_circle(radius, color, position):
    #Cria um círculo com o raio, cor e posição especificados.
    diameter = radius * 2
    surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (radius, radius), radius)
    rect = surface.get_rect()
    rect.topleft = position
    return surface, rect

def random_color():
    #Gera uma cor aleatória.
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_position(max_x, max_y):
    #Gera uma posição aleatória dentro da área especificada.
    return (random.randint(0, max_x), random.randint(0, max_y))

def random_size(min_size, max_size):
    #Gera um tamanho aleatório dentro do intervalo especificado
    return random.randint(min_size, max_size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Formas Geométricas Aleatórias")
    clock = pygame.time.Clock()

    shapes = []

    for _ in range(NUM_SHAPES):
        if random.choice([True, False]):
            width = random_size(MIN_SIZE, MAX_SIZE)
            height = random_size(MIN_SIZE, MAX_SIZE)
            rect_surface, rect_rect = create_rectangle(width, height, random_color(), random_position(WIDTH - width, HEIGHT - height))
            shapes.append((rect_surface, rect_rect))
        else:
            radius = random_size(MIN_RADIUS, MAX_RADIUS)
            circle_surface, circle_rect = create_circle(radius, random_color(), random_position(WIDTH - 2 * radius, HEIGHT - 2 * radius))
            shapes.append((circle_surface, circle_rect))

    running = True
    transition_time = 0
    transition_duration = 2000  # 2000 milissegundos = 2 segundos
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        current_time = pygame.time.get_ticks()
        if current_time - transition_time >= transition_duration:
            transition_time = current_time
            for i, (shape_surface, shape_rect) in enumerate(shapes):
                if random.choice([True, False]):
                    width = random_size(MIN_SIZE, MAX_SIZE)
                    height = random_size(MIN_SIZE, MAX_SIZE)
                    rect_surface, rect_rect = create_rectangle(width, height, random_color(), random_position(WIDTH - width, HEIGHT - height))
                    shapes[i] = (rect_surface, rect_rect)
                else:
                    radius = random_size(MIN_RADIUS, MAX_RADIUS)
                    circle_surface, circle_rect = create_circle(radius, random_color(), random_position(WIDTH - 2 * radius, HEIGHT - 2 * radius))
                    shapes[i] = (circle_surface, circle_rect)

        for shape_surface, shape_rect in shapes:
            shape_surface.set_alpha(int(255 * (1 - (current_time - transition_time) / transition_duration)))
            screen.blit(shape_surface, shape_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()