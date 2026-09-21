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

animal = Animal("Zwierzę")
dog_1 = Dog("Burek")
dog_2 = Dog("Azor")
cat_1 = Cat("Mruczek")
cat_2 = Cat("Klakier")

animal.make_sound()
dog_1.make_sound()
dog_2.make_sound()
cat_1.make_sound()
cat_2.make_sound()
