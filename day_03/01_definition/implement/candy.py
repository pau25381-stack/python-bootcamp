class Candy:
    def __init__(self, flavor):
        self.flavor = flavor

choco1 = Candy("Chocolate")
choco2 = Candy("Chocolate")
milk = Candy("Milk")

print(choco1 == milk)
print(choco1 == choco2)