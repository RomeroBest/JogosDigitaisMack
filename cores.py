import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

def create_scales(height):
    red_scale_surface   = pygame.surface.Surface((640, height)) 
    green_scale_surface = pygame.surface.Surface((640, height)) 
    blue_scale_surface  = pygame.surface.Surface((640, height)) 
    for x in range(640):
        c = int((x/639.)*255.)
        red   = (c, 0, 0) 
        green = (0, c, 0) 
        blue  = (0, 0, c)
        line_rect = Rect(x, 0, 1, height) 
        pygame.draw.rect(red_scale_surface, red, line_rect) 
        pygame.draw.rect(green_scale_surface, green, line_rect) 
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface 

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    screen.blit(red_scale, (0, 00)) 
    screen.blit(green_scale, (0, 80)) 
    screen.blit(blue_scale, (0, 160))

    x, y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                color[component] = int((x/639.)*255.)
        pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))

    for component in range(3):
        pos = ( int((color[component]/255.)*639), component*80+40 )
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    # Garantir que os valores de cor estejam no intervalo 0-255
    color = [max(0, min(c, 255)) for c in color]
    
    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.update()