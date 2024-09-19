import random

class NaveEspacial:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = (0, 0)
        self.direction = 0
        self.speed = 0
        self.shield = 100
        self.energy = 100

    def move(self):
        print(f"{self.name} está se movendo para a frente.")

    def turn(self, direction):
        if direction.lower() == 'esquerda':
            self.direction -= 90
        elif direction.lower() == 'direita':
            self.direction += 90
        print(f"{self.name} virou para a {direction}.")

    def shoot(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} lançou um projétil.")
        else:
            print(f"{self.name} não tem energia suficiente para atirar.")

    def hit(self, damage):
        self.shield -= damage
        if self.shield <= 0:
            self.alive = False
            print(f"{self.name} foi destruída.")
        else:
            print(f"{self.name} foi atingida! Escudo restante: {self.shield}")

    def recharge(self):
        self.energy = 100
        print(f"{self.name} recarregou sua energia.")

def recarga_aleatoria(nave):
    if random.randint(1, 10) > 7:  # 30% de chance de recarregar
        nave.recharge()
        print(f"{nave.name} recebeu uma recarga aleatória de energia!")

def jogo():
    nave1 = NaveEspacial("Falcon")
    nave2 = NaveEspacial("Eagle")

    jogadores = [nave1, nave2]
    turno = 0

    while nave1.alive and nave2.alive:
        jogador_atual = jogadores[turno % 2]
        oponente = jogadores[(turno + 1) % 2]

        print(f"\nTurno do jogador: {jogador_atual.name}")

        # Exemplo de ação do jogador
        jogador_atual.shoot()
        oponente.hit(20)

        # Recarga aleatória de energia
        recarga_aleatoria(jogador_atual)

        # Verificar se o oponente foi destruído
        if not oponente.alive:
            print(f"{jogador_atual.name} venceu!")
            break

        turno += 1

# Iniciar o jogo
jogo()
