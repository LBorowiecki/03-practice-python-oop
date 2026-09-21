class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def describe(self):
        print(f'{self.name} pracuje na stanowisku {self.position}')
    
class Teacher(Employee):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject
    
    def describe(self):
        print(f'{self.name} to {self.position} i uczy {self.subject}')

employee_1 = Employee("Jan Kowalski", "Menadżer")
employee_2 = Employee("Michał Nowak", "Sprzedawca")
teacher_1 = Teacher("Anna Nowak", "nauczyciel", "matematyka")
teacher_2 = Teacher("Tomasz Lewandowski", "nauczyciel", "geografia")

employee_1.describe()
employee_2.describe()
teacher_1.describe()
teacher_2.describe()