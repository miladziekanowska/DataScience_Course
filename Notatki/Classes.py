class Car:
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []
    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True

c1 = Car("Czerwony", 450000, "Ferrari")
c2 = Car("Zielony", 75000, "Opel")
print(c1.color, c2.color)
print(c1.running)
c1.switch()
print(c1.running)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []
        self.mean = 0.0

    def add_grade(score: float):
        if score in [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]:
            grades.append(score)
            mean = sum(grades) / len(grades)
        else:
            return "Score not in range"

s1 = Student("Miła", "Dziekanowska")
s1.add_grade(4.5)
print(s1.mean)