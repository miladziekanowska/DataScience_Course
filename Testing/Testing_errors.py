def dec_to_bin(value: int) -> list:
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]


x = 10

try:
    print(x / 0)
except ZeroDivisionError:   # expect: <-- instrukcje dla wystąpienia dowolnego błędu
    print("Próbowałeś/aś dzielić przez zero.")
finally:
    # Wykonaj to zawsze na końcu - niezależnie od powyższych bloków
    print("WYKONAŁEM SIĘ!")

a = [10, 20, 3, 4, "Ala ma kota", True, 3, 4, 12, "Piesek", "XD", 20]
errors_value = []

for i in range(len(a)):
    try:
        a[i] = dec_to_bin(a[i])
    except TypeError:
        errors_value.append(a[i])




try:
    print(10 / 0)
    print("Ala ma " + 5 + "kotów.")
except ZeroDivisionError:
    print("Próbowano dzielić przez zero")
except TypeError:
    print("Wystąpił problem z typem danych")

# Do zadania nr 4 z pracy domowej dopisz zabezpeczenie, jeżeli użytkownik poda
# informację, której nie można konwertować na int

try:
    n = int(input("Podaj liczbę: "))
    summary = 0

    while n >= 0:
        summary += n
        n = int(input("Podaj liczbę: "))

    print(f"Suma podanych liczb to: {summary}")

except ValueError:
    print("Podano błędną informację")





# Rozwiń funkcjonalność zadania z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontynuuj działanie
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)