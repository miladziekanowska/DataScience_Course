def summary (*args) -> None:
    print(f"Elements: {args}")
    result = 0
    for i in args:
        result += i
    return result

#Jeśli w funkcji zostanie dodana niewiadoma liczba argumentów, *args przyjmie dowolną liczbę argumentów i będzie
# traktował jak krotkę
# upakowana zmienna args

#**kwargs

#kwargs zwraca słownik, przez co możemy dodawać dużo więcej informacji i zmian oraz stosować więcej funkcjonalności

def fun_with_option(**kwargs):
    if kwargs.get("power", -1) == -1:
        print("Nie opcji potęgi")
    else:
        print(2 ** kwargs.get("power", -1))

    if kwargs.get("sqrt", False):
        print("Chciałeś pierwiastkować?")
    else:
        print("Opcja sqrt jest na false")