class Animal:
    def __init__(self, name):
        self.legs_count = 0.0
        self.eyes_count = 0.0
        self.name = name
        self.is_alive = True

    def __str__(self):
        return self.name

a1 = Animal("Koczkodan")
print(str(a1))
