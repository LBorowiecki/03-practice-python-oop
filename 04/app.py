class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Zwierzę wydaje dźwięk")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} szczeka: Hau! Hau!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} miauczy: Miau! Miau!")

animals = [Animal("Zwierzę"), Dog("Burek"),  Dog("Azor"), Cat("Mruczek"), Cat("Klakier")]

for i in animals:
    i.make_sound()