# 1. Utwórz zmienne: x i y oraz przypisz do nich dowolne liczby.
#  Następnie wyświetl wszystkie operacje arytmetczne z wykorzystaniem zmiennych

#  2. Utwórz zmienną tekstową (dowolny) tekst, a następnie dopisz do niego (do zmiennej)
#     Tekst: "a kot ma pierdolca"

# #1

x = 4
y = 5

print("Dodawanie: ", x + y,
      "\nOdejmowanie: ", x - y,
      "\nMnożenie: ", x * y,
      "\nDzielenie: ", x / y,
      "\nPotęgowanie: ", x ** y,
      "\nDzielenie bez reszty: ", x // y,
      "\nReszta z dzielenia: ", x % y)
#
# #2

what = "Ala ma kota, "
what += "kot ma pierdolca"
print(what)


#  3. Napisać program, który przyjmie od użytkownika dwie wartości zmiennoprzecinkowe (float)
#      a nastęnie wyświetli ich: sumę, różnicę oraz iloczyn

#  4. Napisać program, który przyjmie od użytkownika tekst jako "nazwę produktu" oraz
#     jego ilośc a następnie wyświetli komunikat w formacie:
#     produkt - ilość

# #3

value1 = float(input("Wprowadź pierwszą liczbę: "))
value2 = float(input("Wprowadź drugą liczbę: "))

print("Suma: ", value1 + value2,
      "\nRóżnica: ", value1 - value2,
      "\nIloczyn: ", value1 * value2)

#4

product = input("Wprowadź nazwę produktu: ")
quantity = input("Wprowadź ilość: ")
print(product, " - ", quantity)


# 5. Użytkownik podaje liczbę, a nastęnie dostaje odpowiedź czy podana liczba
#     jest parzysta/nieparzysta.

# 6. Użytkownik podaje liczbę, a nastęnie program:
#     Wyświetli "Pif Paf", jeżeli podana liczba jest podzielna przez 3 i 5
#     Wyświetli "Pif", jeżeli podana liczba jest podzielna tylko przez 3
#     Wyświetli "Paf", jeżeli podana liczba jest podzielna tylko przez 5
#     Wyświetli komunikat "Twoja liczba to: " + podana liczba, jeżeli nie spełniono
#     żadnego z powyższych warunków.

#5

number = int(input("Wprowadź liczbę: "))
if number % 2 == 0:
      print("Twoja liczba jest parzysta.")
else: print("Twoja liczba jest nieparzysta.")

#6

entry = int(input("Wprowadź liczbę: "))
if entry % 3 == 0 and entry % 5 == 0:
      print ("Pif Paf")
elif entry % 3 == 0:
      print("Pif")
elif entry % 5 == 0:
      print("Paf")
else: print("Twoja liczba to: ", entry)

# 7. Napisz funkcję is_even, która przyjmuje jeden argument
#     A następnie zwraca True - jeżeli liczba jest parzysta,
#     w przeciwnym razie False
#
#     Wykorzystaj nową funkcję do poprzedniego zadania
#     (tam gdzie użytkownik podawał liczbę, a następnie otrzymywał komunikat
#      liczba parzysta/nieparzysta)

# 8. Napisz funkcję my_pow, która pozwoli na zwrócenie potęgi wybranej liczby
#     do wybranej potęgi. Liczbe oraz potegę podajemy jako argumenty do tej fukncji

#7.
def is_even(value):
      value = int(input("Wprowadź liczbę: "))
      if number % 2 == 0:
            value("Twoja liczba jest parzysta.")
      else:
            value("Twoja liczba jest nieparzysta.")

#8.

def my_pow(val, power):
      val = int(input("Podaj liczbę do spotęgowania: "))
      power = int(input("Podaj potęgę: "))
      return val ** power
