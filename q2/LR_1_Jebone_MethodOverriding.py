class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

    def make_sound(self):
        print(self.name, "makes a sound.")

class Lion(Animal):
    def eat(self):
        print(self.name, "is eating fresh meat.")

    def make_sound(self):
        print(self.name, "roars loudly!")

class Elephant(Animal):
    def eat(self):
        print(self.name, "is eating grass and fruits.")

    def make_sound(self):
        print(self.name, "trumpets!")

class Monkey(Animal):
    def eat(self):
        print(self.name, "is eating bananas.")

    def make_sound(self):
        print(self.name, "chatters!")


lion = Lion("Leo")
elephant = Elephant("Ella")
monkey = Monkey("Milo")

zoo_animals = [lion, elephant, monkey]

for zoo_animal in zoo_animals:
    zoo_animal.eat()
    zoo_animal.make_sound()
    print()