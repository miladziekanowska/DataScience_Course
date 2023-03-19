# Napisać dekorator, dla funkcji która nie przyjmuje żadnych argumentów
# oraz niczego nie zwraca, którego zadaniem jest wyświetlenie po wywołaniu
# funkcji napisu "--- KONIEC ---"

# Sprawdzić w praktyce dla dowolnej utworzonej przez Was funkcji.
#
# def end_decorator(func):
#     def wrapper():
#         func()
#         print("--- KONIEC ---")
#     return wrapper
#
#
# @end_decorator
# def my_date() -> None:
#     print(f"Dzisiaj jest: 19-03-2023")
#
# my_date()


# Napisz klasę o nazwie Product, która zawiera pole:
#     - nazwa (str)
#     - kategoria (str)
#     - sn (str)
#     - price (float)
#
# Zmienne sn oraz price są prywatne,
#     a dostęp do nich jest możliwy dzięki getter/setter
#
# Dodatkowo nie można ustawić price na wartość mniejszą niż 0.01
#     (próba ustawienia wartości mniejszej niż 0.01 powoduje ustawienie 0.01)

class Product:

    def __init__(self, name, category, sn, price):
        self.name = name
        self.category = category
        self.__sn = sn
        self.__price = price

    @property
    def sn(self):
        return self.__sn

    @property
    def price(self):
        return self.__price

    @sn_setter
    def sn(self, new_sn):
        self.__sn = new_sn
    @price_setter
    def price(self, new_price):
        if new_price >= 0.01:
            self.__price = new_price
        else:
            self.__price = 0.01



# Napisz funkcję, która jako PIERWSZY argument przyjmuje rodzaj operacji
#     "suma", "różnica", "iloczyn"
# a następnie wykona sumowanie/odejmowanie/mnożenie wszystkich argumentów
# podanych po pierwszym. Ilość argumentów do obliczeń może być dowolna

def operations(operation, *args):
    result = args[0]
    if len(args) >= 2:
        if operation == "suma":
            for i in range(1, len(args)):
                result += args[i]
        elif operation == "różnica":
            for i in range(1, len(args)):
                result -= args[i]
        if operation == "iloczyn":
            for i in range(1, len(args)):
                result *= args[i]
        return result
    else:
        return args[0]