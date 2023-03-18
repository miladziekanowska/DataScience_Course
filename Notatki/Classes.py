class Car:
    #określamy z czego składa się obiekt
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    #określamy co ma się wyświetlać, jeśli wywołamy obiekt jako to co między __
    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"

    def __float__(self):
        return self.price

    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True

c1 = Car("Czerwony", 450000, "Ferrari")
c2 = Car("Zielony", 75000, "Opel")
print(str(c1))
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

    def add_grade(self, score: float):
        if score in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades.append(score)
            self.mean = sum(self.grades) / len(self.grades)
        else:
            return "Score not in range"

    def __str__(self):
        return f"{self.name} {self.surname.lower()} - {self.mean}"

    def __int__(self):
        return int(sum(self.grades))

    def __float__(self):
        return self.mean

s1 = Student("Miła", "Dziekanowska")
s1.add_grade(4.0)
s1.add_grade(5.0)
s1.add_grade(3.5)
print(str(s1))
print(int(s1))
print(float(s1))


