import pygame
import random

# Constantes
WIDTH, HEIGHT = 800, 600
NUM_RECTANGLES = 6

# Cores
WHITE = (255, 255, 255)

def lerp(a, b, t):
    """Função de lerp para interpolar entre dois valores."""
    return a + (b - a) * t

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Retângulos com Cores Aleatórias")
    clock = pygame.time.Clock()

    rectangles = []
    for i in range(NUM_RECTANGLES):
        y = i * (HEIGHT // NUM_RECTANGLES)
        height = HEIGHT // NUM_RECTANGLES
        rectangle = pygame.Rect(0, y, WIDTH, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rectangles.append((rectangle, color, target_color))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for i, (rectangle, color, target_color) in enumerate(rectangles):
            t = (pygame.time.get_ticks() + i * 1000) / 3000
            t = t % 1
            new_color = (int(lerp(color[0], target_color[0], t)), int(lerp(color[1], target_color[1], t)), int(lerp(color[2], target_color[2], t)))
            pygame.draw.rect(screen, new_color, rectangle)

            if t > 0.99:
                rectangles[i] = (rectangle, target_color, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()