import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Definindo constantes
LARGURA_TELA = 800
ALTURA_TELA = 600
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Configurando a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Nave Espacial")

# Classe NaveEspacial herda de pygame.sprite.Sprite
class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name, position=(400, 300), speed=5):
        super().__init__()
        
        # Atributos da nave
        self.name = name
        self.alive = True
        self.position = position
        self.direction = 0  # Inicialmente em 0 graus
        self.speed = speed
        self.shield = 100
        self.energy = 100
        
        # Desenho da nave (usando um retângulo)
        self.image = pygame.Surface((50, 30))
        self.image.fill(BRANCO)
        
        # Definir o rect para controlar a posição da nave
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        # Movimentação com base nas teclas pressionadas
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        # Manter a nave dentro dos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA

# Função principal do jogo
def jogo():
    # Configura o relógio para controlar o FPS
    relogio = pygame.time.Clock()

    # Criação da nave
    nave = NaveEspacial(name="Falcon", position=(400, 300), speed=5)

    # Criando um grupo de sprites para facilitar o update e desenho
    todas_as_sprites = pygame.sprite.Group()
    todas_as_sprites.add(nave)

    # Loop principal do jogo
    while True:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizar a nave
        todas_as_sprites.update()

        # Desenhar fundo da tela
        tela.fill(PRETO)

        # Desenhar todos os sprites na tela
        todas_as_sprites.draw(tela)

        # Atualizar a tela
        pygame.display.flip()

        # Controla a quantidade de frames por segundo (FPS)
        relogio.tick(60)

# Executa o jogo
if __name__ == "__main__":
    jogo()
