# 1. Program przyjmuje od użytkownika dwie liczby:
#     1. Liczba prawidłowych odpowiedzi (int)
#     2. Liczba pytań (int)
#     Następnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#     100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
#     69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0

# 2. Napisz funkcję o nazwie show_temp_status, która przyjmuje jeden argument typu float
#    Następnie zwraca str (nie wykonuje print!) zależnie od wartości podanego argumentu:
#     Poniżej 36.4 - wychłodzenie
#     <36.4 36.8> - norma
#     <36.9, 37.0> - stan podgorączkowy
#     Powyżej 3.71 - gorączka

#1.

answers = int(input("Wprowadź liczbę prawidłowych odpowiedzi: "))
questions = int(input("Wprowadź liczbę pytań: "))
percentage = answers / questions * 100
print(percentage, "%")
if percentage <= 100 and percentage >= 90:
    print("5.0")
elif percentage < 89 and percentage >= 76:
    print("4.5")
elif percentage < 76 and percentage >= 70:
    print("4.0")
elif percentage < 70 and percentage >= 60:
    print("3.5")
elif percentage < 60 and percentage >= 50:
    print("3.0")
else: print("2.0")


#2

def show_tem_status(temp):
    if temp < 36.4:
        return "wychłodzenie"
    elif temp >= 36.4 and temp <= 36.8:
        return "norma"
    elif temp > 36.8 and temp <= 37.0:
        return "stan podgorączkowy"
    else:
        return "gorączka"


# 3. Napisz funkcję, która zwróci "odwrotny" indeks wybranego indeksu i tekstu
#     Przyjmowane argumenty:
#     - łańcuch znakowy
#     - indeks (z przedziału podanego tekstu)
#     Zwraca:
#     - odwrotny indeks
#
#  Przykładowo:
#  fun("Ala ma kota", 11) zwraca -1
#  fun("HELLO", 2) zwraca -3

#3.

def minus_index(words, index):
    if  0 <= index <= (len(words) - 1):
        return index - len(words)
    else: return -999


print(minus_index("guma", 2))
print(minus_index("Dzień dobry", 4))