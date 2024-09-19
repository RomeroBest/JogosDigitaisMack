import pygame
import sys
import random
import math
from pygame.locals import QUIT, KEYDOWN, K_SPACE

# Inicializa o Pygame
pygame.init()

# Definindo constantes
LARGURA_TELA = 800
ALTURA_TELA = 600
PRETO = (0, 0, 0)

# Configurando a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Nave Espacial")

# Classe para gerenciar os disparos
class Disparo(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Cor do disparo
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, -angle)

    def update(self):
        # Movimento do disparo na direção da nave
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        # Remove o disparo quando ele sair da tela
        if not tela.get_rect().colliderect(self.rect):
            self.kill()

# Classe para o objeto (astro) que se move aleatoriamente
class Astro(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Ajusta o tamanho
        self.rect = self.image.get_rect(
            center=(random.randint(0, LARGURA_TELA), random.randint(0, ALTURA_TELA))
        )
        self.speed = random.uniform(2.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        # Movimento contínuo do astro
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        # O astro reaparece nas extremidades opostas
        if self.rect.left > LARGURA_TELA:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = LARGURA_TELA
        if self.rect.top > ALTURA_TELA:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = ALTURA_TELA

# Classe NaveEspacial herda de pygame.sprite.Sprite
class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name, image_path, position=(400, 300), speed=5):
        super().__init__()
        
        # Atributos da nave
        self.name = name
        self.alive = True
        self.position = position
        self.speed = speed
        self.direction = 0  # Direção da nave em graus
        self.shield = 100
        self.energy = 100
        
        # Carrega a imagem da nave
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (150, 110))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        # Movimento da nave
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.direction += 5
        if teclas[pygame.K_RIGHT]:
            self.direction -= 5
        if teclas[pygame.K_UP]:
            self.rect.x += self.speed * math.cos(math.radians(self.direction))
            self.rect.y -= self.speed * math.sin(math.radians(self.direction))
        if teclas[pygame.K_DOWN]:
            self.rect.x -= self.speed * math.cos(math.radians(self.direction))
            self.rect.y += self.speed * math.sin(math.radians(self.direction))

        # Rotacionar a nave na direção em que ela está apontando
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Permitir que a nave atravesse a tela
        if self.rect.left > LARGURA_TELA:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = LARGURA_TELA
        if self.rect.top > ALTURA_TELA:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = ALTURA_TELA

# Função principal do jogo
def jogo():
    # Configura o relógio para controlar o FPS
    relogio = pygame.time.Clock()

    # Caminho para a imagem da nave (Millennium Falcon)
    caminho_imagem_nave = r"C:\Users\1168631\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\MillenniumFalcon.png"  # Substitua pelo caminho correto

    # Caminho para a imagem de fundo (galáxia)
    caminho_fundo = r"C:\Users\1168631\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\galaxia.jpg"  # Substitua pelo caminho correto

    # Caminho para a imagem do astro (por exemplo, um planeta)
    caminho_astro = r"C:\Users\1168631\OneDrive\Programacao\ADS\2SEM\JOGOS DIGITAIS\CODIGOS\assets\asteroide.png"  # Substitua pelo caminho correto

    # Carrega a imagem de fundo
    fundo = pygame.image.load(caminho_fundo).convert()
    fundo = pygame.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA))

    # Criação da nave
    nave = NaveEspacial(name="Falcon", image_path=caminho_imagem_nave, position=(400, 300), speed=5)

    # Criação do astro
    astro = Astro(image_path=caminho_astro)

    # Grupos de sprites
    todas_as_sprites = pygame.sprite.Group()
    todas_as_sprites.add(nave)
    todas_as_sprites.add(astro)

    tiros = pygame.sprite.Group()

    # Loop principal do jogo
    while True:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    # Criar um disparo da posição da nave
                    tiro = Disparo(nave.rect.center, nave.direction)
                    tiros.add(tiro)
                    todas_as_sprites.add(tiro)

        # Atualizar todos os sprites
        todas_as_sprites.update()

        # Desenhar o fundo
        tela.blit(fundo, (0, 0))

        # Desenhar todos os sprites na tela
        todas_as_sprites.draw(tela)

        # Atualizar a tela
        pygame.display.flip()

        # Controla a quantidade de frames por segundo (FPS)
        relogio.tick(60)

# Executa o jogo
if __name__ == "__main__":
    jogo()