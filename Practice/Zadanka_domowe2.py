# Zadanie 01
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych,
# a zwraca wartość int jako największa liczba z listy (nie wolno używać max).
# Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)

def largest_number(*args):
    try:
        largest = None
        for n in args:
            if largest is None:
                largest = n
            elif n > largest:
                largest = n
        print(largest)
    except TypeError:
        print("Wystąpił problem z typem danych, wprowadź tylko dane int")


# Zadanie 02
# Napisz moduł, który będzie posiadał funkcje obliczające:
# Funkcje kwadratową (zwraca listę rozwiązań)
# Pierwiastek drugiego stopnia z podanej liczby
# N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)

from Squares_module.Squares import square_func, harmonic_seq, square_element

square_func(1,2,4,5)
harmonic_seq(4)
square_element(4)

# Zadanie 03
# Napisz program, który narysuje trójkąt zależnie od podanego n
# Np. n = 3 to wynik jest
# *
# **
# ***
# Dodaj dekorator, który dodatkowo dopisze "-----------" na dole trójkąta oraz policzy liczbę *


def bottom(func):
    def wrapper(n):
        func(n)
        print("-------------------")
        print(f"There are {sum(range(n+1))} *")
    return wrapper

@bottom
def triangle(n: int):
    a = 1
    while a <= n:
        print("*" * a)
        a += 1


