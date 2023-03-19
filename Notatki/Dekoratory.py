#dekoratory

def say_hi(name: str) -> None:
    print(f"Hello, {name}")

def get_name(name: str):
    return say_hi(name)

# print(get_name("Miła"))

def trigger_info(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        return func(*args, **kwargs))
    return wrapper

@trigger_info
def my_add(a,b):
    return a+b

@trigger_info
def my_sub(a,b)
    return a-b


#dekorato properties
    #stosujemy do zabezpieczenia programu

class Person:
    def __init__(self, f_name, l_name, age): -> None:\
        self.f_name = f_name
        self.l_name = l_name
        self.__age = age

    @property
    def age(self):    #tzw getter
        return self.__age

    #setter
    @age.setter
    def age(self, new_age):
        self.__age = new_age



p1 = Person("Jan", "Kowalski", 30)
#wartości są publiczne bo możemy wyciągnąć informacje o obiekcie
print(p1.age)

#aby zrobić informację na prywatną, dodajemy __ na przodzie (jak w age) i wtedy te informacje nie są publiczne
# możemy je wydobyć wewnątrz klasy i z funkcji wewnątrz klasy, ale poza klasą nie mamy do nich dostępu (ochrona informacji)
# teraz jeśli chcemy normalnie wydobyć age, nie da się, bo nie mamy bezpośredniego
# ale używając gettera, jest to jednostka pośrednia, pomocnik, który pozwala nam wydobyć pośrednio informacje
# aby zmienic taką zablokowaną wartość, musimy użyć setter


