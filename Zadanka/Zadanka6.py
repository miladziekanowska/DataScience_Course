# Napisać dekorator, dla funkcji która nie przyjmuje żadnych argumentów
# oraz niczego nie zwraca, którego zadaniem jest wyświetlenie po wywołaniu
# funkcji napisu "--- KONIEC ---"

# Sprawdzić w praktyce dla dowolnej utworzonej przez Was funkcji.

def end_decorator(func):
    def wrapper():
        func()
        print("--- KONIEC ---")
    return wrapper


@end_decorator
def my_date() -> None:
    print(f"Dzisiaj jest: 19-03-2023")

my_date()