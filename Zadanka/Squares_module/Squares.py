# Zadanie 02
# Napisz moduł, który będzie posiadał funkcje obliczające:
# Funkcje kwadratową (zwraca listę rozwiązań)
# Pierwiastek drugiego stopnia z podanej liczby
# N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)


def square_func(*args) -> list:
    for n in args:
        return n ** 2

def square_element(n: float) -> float:
    return n ** (1/2)

def harmonic_seq(n: int) -> float:
    return 1 / n

