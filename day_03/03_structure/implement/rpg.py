from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()


class Mage(Character):
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


class Archer(Character):
    def attack(self, other):
        damage = 10
        other.health -= damage


class Bard(Character):
    def __init__(self, health=50, defense=5, charisma=20):
        super().__init__(health, defense)
        self.charisma = charisma

    def attack(self, other):
        damage = self.charisma // 2
        other.health -= damage


# Example usage
mage = Mage()
archer = Archer()
bard = Bard()

archer.attack(mage)
print("Mage health:", mage.health)

bard.attack(archer)
print("Archer health:", archer.health)

mage.attack(bard)
print("Bard health:", bard.health, "Mage magic:", mage.magic)
