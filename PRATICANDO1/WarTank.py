import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i Blindagem, %i Tiros)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DESTRUÍDO)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "atira em", enemy.name)
            enemy.hit()
        else:
            print(self.name, "Não há mais tiro!")

    def hit(self):
        self.armor -= 20
        print(self.name, "foi atingido")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "Boom!")


# Criando cinco tanques e armazenando-os em uma lista.
tanques = [Tank("PanzerIII"), Tank("Flakpanzer IV Ostwind"), Tank("Panzer 38(t)"),
            Tank("Sturmtiger"), Tank("M18 Hellcat")]

# Simulação da batalha até restar apenas um tanque.
while len(tanques) > 1:
    # Seleciona aleatoriamente um tanque para atacar
    atacante_index = random.randint(0, len(tanques) - 1)
    atacante = tanques[atacante_index]
    
    # Seleciona aleatoriamente um tanque para ser atacado (que não seja o atacante)
    defensor_index = random.choice([i for i in range(len(tanques)) if i != atacante_index])
    defensor = tanques[defensor_index]
    
    # Atacante atira no defensor
    atacante.fire_at(defensor)
    
    # Verifica se o defensor explodiu
    if not defensor.alive:
        tanques.pop(defensor_index)
    
    # Exibe o estado atual dos tanques
    print("\nEstado atual dos tanques:")
    for tanque in tanques:
        print(tanque)

# Fim da simulação
print("\nFim da batalha! O tanque vencedor é:", tanques[0])
