class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def describe(self):
        return f'{self.name} pracuje na stanowisku {self.position}'
    
class Teacher(Employee):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject
    
    def describe(self):
        return f'{self.name} to {self.position} i uczy {self.subject}'

employee_1 = Employee("Jan Kowalski", "Menadżer")
employee_2 = Employee("Michał Nowak", "Sprzedawca")
teacher_1 = Teacher("Anna Nowak", "nauczyciel", "matematyka")
teacher_2 = Teacher("Tomasz Lewandowski", "nauczyciel", "geografia")

print(employee_1.describe())
print(employee_2.describe())
print(teacher_1.describe())
print(teacher_2.describe())