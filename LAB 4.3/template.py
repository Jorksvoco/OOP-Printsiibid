from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        self.max_health = health

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        
        c1_alive = self.hit(c1, c2)
        c2_alive = self.hit(c2, c1)
        
        if c1_alive == c2_alive:  # mõlemad elus või surnud
            return -1
        elif c2_alive and not c1_alive:
            return c2_index
        else:
            return c1_index

    def hit(self, attacker, defender):
        pass

class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = defender.max_health  # taasta elu
            return True
        return False

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health > 0
# proov
creatures = [Creature(1, 2), Creature(1, 3)]
game = TemporaryDamageCardGame(creatures)
print(game.combat(0, 1))  # -1

creatures = [Creature(1, 2), Creature(1, 3)]
game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))  # -1
print(game.combat(0, 1))  # 1

creatures = [Creature(2, 2), Creature(2, 2)]
game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))  # -1    