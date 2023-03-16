# Napisz funkcję, która przyjmuja łańcuch znakowy
#     (dla ułtawienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#     Klucz - litera
#     Wartość - ilość wystąpień litery w tekście
# Przykładowo: dla klucza "l" wartości to 2


slowo = str(input("Wprowadź wyrażenie: "))
litery = {}
for l in range(len(slowo)):
    if slowo[l] not in litery.keys():
        litery[slowo[l]] = 1
    else:
        litery[slowo[l]] = litery[slowo[l]] + 1

print(slowo, litery)
