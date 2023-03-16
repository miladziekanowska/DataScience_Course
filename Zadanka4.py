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


# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)

liczba = int(input("Wprowadź swoją liczbę: "))
n = 0
while n <= liczba:
    print(n)
    n += 2

# Wykorzystując pętle while, program wyświetli wszystkie pierwiastki
#     liczb od 10 do 2 (włącznie) (n ** 0.5)

a = 10
while a in range(10, 1, -1):
    print (a ** 0.5)
    a -= 1

# Napisz program, który sumuje wszystkie liczby całkowite z danego przedziału
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik - 33

start_value = int(input("Start value: "))
end_value = int(input("End value: "))
start_sum = 0

for b in range(start_value, end_value +1):
     start_sum += b

print(start_sum)