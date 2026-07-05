from .character import Character


class Archer(Character):
    '''This is Archer'''
    def attack(self, other):
        damage = 10
        other.health -= damage