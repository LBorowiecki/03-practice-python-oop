class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Cześć, mam na imię {self.name}, mam {self.age} lat i mieszkam w {self.city}")

person_1 = Person("Jan", 25, "Warszawa")
person_2 = Person("Anna", 30, "Kraków")
person_3 = Person("Piotr", 35, "Gdańsk")

person_1.introduce()
person_2.introduce()
person_3.introduce()
