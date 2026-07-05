from .character import Character

class Mage(Character):
    '''This is Mage'''
    def __init__(self, health=100, defense=10, magic=50):
        super().__init__(health, defense)
        self.magic = magic

    def attack(self, other):
        if self.magic >= 10:
            damage = 20
            other.health -= damage
            self.magic -= 10
        else:
            print("Not enough magic!")