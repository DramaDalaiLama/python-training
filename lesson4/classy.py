class Animal(object):
    def __init__(self, species):
        self.species = species

class Cow(Animal):
    def __init__(self, species, name):
        self.name = name

class Chicken(Animal):
    def __init__(self, species, name):
        self.name = name

class Barnyard(object):
    def add_animal(self, item):
        self.animals.append(item)

    def remove_animal(self, item):
        self.animals.remove(item)

    def list_animals(self):
        for animal in self.animals:
            print animal.name

    def __init__(self):
        self.animals = []

test = Cow(species="auroch", name="Wussy")
test1 = Chicken(species="bird", name="Chippy")

barn = Barnyard()

barn.add_animal(test)
barn.add_animal(test1)

barn.list_animals()

barn.remove_animal(test)

barn.list_animals()
