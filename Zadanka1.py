# 1. Utwórz zmienne: x i y oraz przypisz do nich dowolne liczby.
#    Następnie wyświetl wszystkie operacje arytmetczne z wykorzystaniem zmiennych

# 2. Utwórz zmienną tekstową (dowolny) tekst, a następnie dopisz do niego (do zmiennej)
#    Tekst: "a kot ma pierdolca"

#1

x = 4
y = 5

print("Dodawanie: ", x + y,
      "\nOdejmowanie: ", x - y,
      "\nMnożenie: ", x * y,
      "\nDzielenie: ", x / y,
      "\nPotęgowanie: ", x ** y,
      "\nDzielenie bez reszty: ", x // y,
      "\nReszta z dzielenia: ", x % y)

#2

what = "Ala ma kota, "
what += "kot ma pierdolca"
print(what)


# 3. Napisać program, który przyjmie od użytkownika dwie wartości zmiennoprzecinkowe (float)
#     a nastęnie wyświetli ich: sumę, różnicę oraz iloczyn

# 4. Napisać program, który przyjmie od użytkownika tekst jako "nazwę produktu" oraz
#     jego ilośc a następnie wyświetli komunikat w formacie:
#     produkt - ilość

#3

value1 = float(input("Wprowadź pierwszą liczbę: "))
value2 = float(input("Wprowadź drugą liczbę: "))

print("Suma: ", value1 + value2,
      "\nRóżnica: ", value1 - value2,
      "\nIloczyn: ", value1 * value2)

#4

product = input("Wprowadź nazwę produktu: ")
quantity = input("Wprowadź ilość: ")
print(product, " - ", quantity)