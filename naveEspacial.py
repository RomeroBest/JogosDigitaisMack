import pygame
import sys
import random
import math
from pygame.locals import QUIT, KEYDOWN, K_SPACE

# Inicializar Pygame
pygame.init()

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurar a tela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Ship Game")

# Carregar imagens
explosion_images = [pygame.image.load(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\explosao.gif").convert_alpha() for i in range(1, 6)]
game_over_image = pygame.image.load(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\gameover.gif").convert_alpha()
game_over_image = pygame.transform.scale(game_over_image, (400, 200))  # Adjust size as needed

# Classe para a nave espacial
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        super().__init__()
        self.size = size
        self.images = [pygame.transform.scale(img, (size, size)) for img in explosion_images]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=center)
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= 5:  # Trocar quadro a cada 5 quadros do jogo
            self.frame_count = 0
            self.index += 1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]
                self.rect = self.image.get_rect(center=self.rect.center)

# Classe para o tiro para o jogo de nave espacial
class Shot(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Shot color
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, -angle)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

# Classe para o asteroide para o jogo de nave espacial
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.size = random.randint(50, 120)  # Variable size
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.reset_position()

    def reset_position(self):
        # Escolha uma parte da tela para a nave ser respawnada aleatória
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            self.rect.bottom = 0
            self.rect.left = random.randint(0, SCREEN_WIDTH - self.rect.width)
            angle = random.uniform(math.pi/4, 3*math.pi/4)
        elif edge == 'bottom':
            self.rect.top = SCREEN_HEIGHT
            self.rect.left = random.randint(0, SCREEN_WIDTH - self.rect.width)
            angle = random.uniform(5*math.pi/4, 7*math.pi/4)
        elif edge == 'left':
            self.rect.right = 0
            self.rect.top = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            angle = random.uniform(-math.pi/4, math.pi/4)
        else:  # right
            self.rect.left = SCREEN_WIDTH
            self.rect.top = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            angle = random.uniform(3*math.pi/4, 5*math.pi/4)
        
        self.speed = random.uniform(2, 5)
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Se o asteroide estiver fora da tela, redefina sua posição 
        if (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or
            self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT):
            self.reset_position()

# Define a classe Spaceship que herda de Sprite quando criada  
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, name, image_path, position=(400, 300), speed=5):
        super().__init__()
        self.name = name
        self.alive = True
        self.position = position
        self.speed = speed
        self.direction = 0  # Direção do nave em graus
        self.shield = 300  # Valor inicial do escudo
        self.energy = 100

        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (150, 110))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)
        
        # Crie uma máscara para detecção precisa de colisões 
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction += 5
        if keys[pygame.K_RIGHT]:
            self.direction -= 5
        if keys[pygame.K_UP]:
            self.rect.x += self.speed * math.cos(math.radians(self.direction))
            self.rect.y -= self.speed * math.sin(math.radians(self.direction))
        if keys[pygame.K_DOWN]:
            self.rect.x -= self.speed * math.cos(math.radians(self.direction))
            self.rect.y += self.speed * math.sin(math.radians(self.direction))

        # Gire a imagem do nave
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

        # Envolver as bordas da tela
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT

    def lose_shield(self, damage):
        self.shield -= damage
        if self.shield <= 0:
            self.shield = 0
            self.alive = False
            print("The ship has been destroyed!")

# Iniciar o jogo de nave espacial
def game():
    clock = pygame.time.Clock()

    ship_image_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\MillenniumFalcon.png"
    background_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\galaxia.jpg"
    asteroid_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\asteroide.png"

    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ship = Spaceship(name="Falcon", image_path=ship_image_path, position=(400, 300), speed=5)

    asteroids = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(ship)

    # Cria asteroides iniciais aleatórios
    for _ in range(5):
        asteroid = Asteroid(image_path=asteroid_path)
        asteroids.add(asteroid)
        all_sprites.add(asteroid)

    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    font = pygame.font.Font(None, 36)
    game_over = False
    # Loop principal do jogo 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and ship.alive and not game_over:
                    shot = Shot(ship.rect.center, ship.direction)
                    shots.add(shot)
                    all_sprites.add(shot)

        if ship.alive and not game_over:
            all_sprites.update()

            # Verifique a colisão entre asteroides e a nave usando a máscara de colisão
            for asteroid in asteroids:
                if pygame.sprite.collide_mask(ship, asteroid):
                    damage = asteroid.size // 5  # Damage based on asteroid size
                    ship.lose_shield(damage)
                    
                    # Encontre o ponto exato de colisão
                    offset_x = asteroid.rect.x - ship.rect.x
                    offset_y = asteroid.rect.y - ship.rect.y
                    overlap = ship.mask.overlap(asteroid.mask, (offset_x, offset_y))
                    if overlap:
                        collision_point = (ship.rect.x + overlap[0], ship.rect.y + overlap[1])
                        explosion = Explosion(collision_point, size=max(100, asteroid.size))
                        explosions.add(explosion)
                        all_sprites.add(explosion)
                    
                    asteroid.reset_position()

            # Verifique a colisão entre tiros e asteroides
            for shot in shots:
                hit_asteroids = pygame.sprite.spritecollide(shot, asteroids, False, pygame.sprite.collide_mask)
                for asteroid in hit_asteroids:
                    # Encontre o ponto exato de colisão
                    offset_x = asteroid.rect.x - shot.rect.x
                    offset_y = asteroid.rect.y - shot.rect.y
                    overlap = shot.mask.overlap(asteroid.mask, (offset_x, offset_y))
                    if overlap:
                        collision_point = (shot.rect.x + overlap[0], shot.rect.y + overlap[1])
                        explosion = Explosion(collision_point, size=asteroid.size)
                        explosions.add(explosion)
                        all_sprites.add(explosion)
                    
                    shot.kill()
                    asteroid.reset_position()

            if ship.shield <= 0:
                game_over = True
                ship_explosion = Explosion(ship.rect.center, size=200)  # Explosão quando o escudo da nave chega a 0
                explosions.add(ship_explosion)
                all_sprites.add(ship_explosion)

        explosions.update()  # Atualizar explosões separadamente

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        # Contador de escudo de saque
        shield_text = font.render(f"Energia do Escudo: {max(ship.shield, 0)}", True, WHITE)
        screen.blit(shield_text, (10, 10))

        if game_over:
            screen.blit(game_over_image, ((SCREEN_WIDTH - game_over_image.get_width()) // 2,
                                          (SCREEN_HEIGHT - game_over_image.get_height()) // 2))

        pygame.display.flip()
        clock.tick(60)

# Execute o jogo
if __name__ == "__main__":
    game()