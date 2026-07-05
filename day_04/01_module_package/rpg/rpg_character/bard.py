from .character import Character


class Bard(Character):
    '''This is Bard'''
    def __init__(self, health=50, defense=5, charisma=20):
        super().__init__(health, defense)
        self.charisma = charisma

    def attack(self, other):
        damage = self.charisma // 2
        other.health -= damage