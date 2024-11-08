import pygame
import sys
import random
import math
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_i, K_o  # Adicionado as letras

# Inicializar Pygame
pygame.init()
pygame.mixer.init()


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

# Classe para a bomba para o jogo de nave espacial
class SpaceBomb(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Carregar a imagem da bomba
        self.original_image = pygame.image.load(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\bubble.png").convert_alpha()
        # Redimensionar a imagem para um tamanho apropriado (ajuste conforme necessário)
        self.original_image = pygame.transform.scale(self.original_image, (30, 30))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        
        # Tempo de vida da bomba em milissegundos (10 segundos)
        self.lifetime = 10000
        self.spawn_time = pygame.time.get_ticks()
        
        # Movimento aleatório lento
        angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)
        
        # Adicionar rotação
        self.angle = 0
        self.rotation_speed = 2

    def update(self):
        # Atualizar posição
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        # Rotacionar a bomba
        self.angle = (self.angle + self.rotation_speed) % 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        
        # Wrap around nas bordas da tela
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
            
        # Verificar tempo de vida
        if pygame.time.get_ticks() - self.spawn_time > self.lifetime:
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


class RearShot(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((0, 255, 255))  # Cor ciano para diferenciar do tiro frontal
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        # Inverte o ângulo para atirar para trás (adiciona 180 graus)
        self.angle = angle + 180
        self.image = pygame.transform.rotate(self.image, -self.angle)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

# Sons dos disparos 
class GameSounds:
    def __init__(self):
        # Música de fundo
        self.background_music = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\space.mp3")
        
        # Sons de tiro
        self.front_shot_sound = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\laser.mp3")
        self.rear_shot_sound = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\laser.mp3")
        self.bomb_sound = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\laser.mp3")
        
        # Sons de explosão
        self.explosion_sound = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\explosao.mp3")
        self.bomb_explosion_sound = pygame.mixer.Sound(r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\explosao.mp3")
        
        # Configurar volumes
        self.background_music.set_volume(0.3)  # Volume mais baixo para música de fundo
        self.front_shot_sound.set_volume(0.4)
        self.rear_shot_sound.set_volume(0.4)
        self.bomb_sound.set_volume(0.5)
        self.explosion_sound.set_volume(0.6)
        self.bomb_explosion_sound.set_volume(0.7)
    
    def play_background_music(self):
        # Loop infinito para a música de fundo
        self.background_music.play(-1)
    
    def stop_background_music(self):
        self.background_music.stop()


# Iniciar o jogo de nave espacial
def game():
    clock = pygame.time.Clock()

    ship_image_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\MillenniumFalcon.png"
    background_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\galaxia.jpg"
    asteroid_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\asteroide.png"


    # Inicializar sistema de sons
    game_sounds = GameSounds()
    game_sounds.play_background_music()

    # Carregar e redimensionar o cenário para o tamanho da tela
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ship = Spaceship(name="Falcon", image_path=ship_image_path, position=(400, 300), speed=5)

    # Grupos de sprites para os diferentes tipos de asteroides
    asteroids = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(ship)

    # Grupos de sprites para todos os tipos de projéteis
    front_shots = pygame.sprite.Group()  # Tiros frontais
    rear_shots = pygame.sprite.Group()   # Tiros traseiros
    bombs = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    
    # Configurar cooldowns para os diferentes tipos de tiro
    SHOT_COOLDOWN = 250  # 0.25 segundos entre tiros
    BOMB_COOLDOWN = 1000  # 1 segundo entre bombas
    last_front_shot_time = 0
    last_rear_shot_time = 0
    last_bomb_time = 0

    font = pygame.font.Font(None, 36)
    game_over = False

    # Cria asteroides iniciais aleatórios
    for _ in range(5):
        asteroid = Asteroid(image_path=asteroid_path)
        asteroids.add(asteroid)
        all_sprites.add(asteroid)

    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    # Loop principal do jogo 
    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == QUIT:
                game_sounds.stop_background_music()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and ship.alive and not game_over:

                    # Tiro frontal com cooldown
                    if current_time - last_front_shot_time >= SHOT_COOLDOWN:
                        shot = Shot(ship.rect.center, ship.direction)
                        front_shots.add(shot)
                        all_sprites.add(shot)
                        game_sounds.front_shot_sound.play()  # Som de tiro frontal
                        last_front_shot_time = current_time

                # Criar explosão no ponto de colisão
                elif event.key == K_o and ship.alive and not game_over:
                    
                    # Tiro traseiro com cooldown
                    if current_time - last_rear_shot_time >= SHOT_COOLDOWN:
                        rear_shot = RearShot(ship.rect.center, ship.direction)
                        rear_shots.add(rear_shot)
                        all_sprites.add(rear_shot)
                        game_sounds.rear_shot_sound.play()  # Som de tiro traseiro
                        last_rear_shot_time = current_time

                # Criar explosão no ponto de colisão
                elif event.key == K_i and ship.alive and not game_over:

                    # Lançamento de bomba com cooldown
                    if current_time - last_bomb_time >= BOMB_COOLDOWN:
                        bomb = SpaceBomb(ship.rect.center)
                        bombs.add(bomb)
                        all_sprites.add(bomb)
                        game_sounds.bomb_sound.play()  # Som de lançamento da bomba
                        last_bomb_time = current_time

        # Atualizar os sprites
        if ship.alive and not game_over:
            all_sprites.update()

            for bomb in bombs:
                hit_asteroids = pygame.sprite.spritecollide(bomb, asteroids, False, pygame.sprite.collide_mask)
                for asteroid in hit_asteroids:
                    offset_x = asteroid.rect.x - bomb.rect.x
                    offset_y = asteroid.rect.y - bomb.rect.y
                    overlap = bomb.mask.overlap(asteroid.mask, (offset_x, offset_y))
                    if overlap:
                        collision_point = (bomb.rect.x + overlap[0], bomb.rect.y + overlap[1])
                        explosion = Explosion(collision_point, size=max(100, asteroid.size))
                        explosions.add(explosion)
                        all_sprites.add(explosion)
                        game_sounds.bomb_explosion_sound.play()  # Som de explosão da bomba
                    
                    bomb.kill()
                    asteroid.reset_position()
                    break  # Uma bomba só pode destruir um asteroide

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
            for shot in front_shots:
                hit_asteroids = pygame.sprite.spritecollide(shot, asteroids, False, pygame.sprite.collide_mask)
                for asteroid in hit_asteroids:
                    offset_x = asteroid.rect.x - shot.rect.x
                    offset_y = asteroid.rect.y - shot.rect.y
                    overlap = shot.mask.overlap(asteroid.mask, (offset_x, offset_y))
                    if overlap:
                        collision_point = (shot.rect.x + overlap[0], shot.rect.y + overlap[1])
                        explosion = Explosion(collision_point, size=asteroid.size)
                        explosions.add(explosion)
                        all_sprites.add(explosion)
                        game_sounds.explosion_sound.play()  # Som de explosão normal
                    
                    shot.kill()
                    asteroid.reset_position()

            # Verificar colisões dos tiros traseiros com asteroides
            for shot in rear_shots:
                hit_asteroids = pygame.sprite.spritecollide(shot, asteroids, False, pygame.sprite.collide_mask)
                for asteroid in hit_asteroids:
                    offset_x = asteroid.rect.x - shot.rect.x
                    offset_y = asteroid.rect.y - shot.rect.y
                    overlap = shot.mask.overlap(asteroid.mask, (offset_x, offset_y))
                    if overlap:
                        collision_point = (shot.rect.x + overlap[0], shot.rect.y + overlap[1])
                        explosion = Explosion(collision_point, size=asteroid.size)
                        explosions.add(explosion)
                        all_sprites.add(explosion)
                        game_sounds.explosion_sound.play()  # Som de explosão normal
                    
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