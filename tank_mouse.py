import pygame
import math

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Batalha de Tanques")

# Carregar e redimensionar o cenário para o tamanho da tela
background_image = pygame.image.load(r"C:\Users\jorja\Downloads\GRAMA.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Classe do tanque
class Tank(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.original_image = pygame.image.load(r"C:\Users\jorja\Downloads\klipartz.com1.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (100, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(center=(x, y))
        self.name = name
        self.angle = 0
        self.speed = 5

    def update(self, mouse_pos):
        # Calcula a direção para onde o tanque deve se mover
        rel_x, rel_y = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        distance = math.hypot(rel_x, rel_y)

        if distance > 5:  # Evita jittering quando o mouse está muito próximo do tanque
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

            # Move o tanque em direção ao mouse
            self.rect.x += self.speed * rel_x / distance
            self.rect.y += self.speed * rel_y / distance

        # Rotaciona a imagem do tanque para olhar na direção do movimento
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def fire(self, bullets):
        # Função de disparo, cria um novo projétil
        print(f"{self.name} fires!")
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        bullets.add(bullet)

# Classe do projétil
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\jorja\Downloads\CIRCULO.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (15, 15))  # Redimensiona o projétil
        
        # Alterar a cor do projétil para vermelho, por exemplo
        red_color = (255, 0, 0, 255)  # Cor vermelha com transparência total
        self.image.fill(red_color, special_flags=pygame.BLEND_RGBA_MULT)
        
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = 10

    def update(self):
        # Atualiza a posição do projétil
        self.rect.x += self.speed * math.cos(math.radians(-self.angle))
        self.rect.y += self.speed * math.sin(math.radians(-self.angle))

        # Remove o projétil se ele sair da tela
        if self.rect.x < 0 or self.rect.x > screen_width or self.rect.y < 0 or self.rect.y > screen_height:
            self.kill()

# Criando o tanque
tank = Tank("Panzer III", screen_width // 2, screen_height // 2)

# Grupo de sprites para os projéteis
bullets = pygame.sprite.Group()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                tank.fire(bullets)

  
    mouse_pos = pygame.mouse.get_pos()  # Captura a posição atual do mouse
    tank.update(mouse_pos)  # Atualiza a posição e rotação do tanque
    bullets.update()  # Atualiza as posições dos projéteis

    # Desenhando o cenário redimensionado
    screen.blit(background_image, (0, 0))
    
    # Desenhando o tanque e os projéteis sobre o cenário
    tank.draw(screen)
    bullets.draw(screen)
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
