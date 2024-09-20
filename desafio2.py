import pygame
import random

# Constantes
WIDTH, HEIGHT = 800, 600
NUM_RECTANGLES = 6

# Cores
WHITE = (255, 255, 255)

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
        rectangles.append((rectangle, color))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i, (rectangle, color) in enumerate(rectangles):
            if rectangle.collidepoint(mouse_x, mouse_y):
                new_color = (int((mouse_x / WIDTH) * 255), int((mouse_y / HEIGHT) * 255), int(((mouse_x + mouse_y) / (WIDTH + HEIGHT)) * 255))
                rectangles[i] = (rectangle, new_color)
            pygame.draw.rect(screen, rectangles[i][1], rectangle)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()