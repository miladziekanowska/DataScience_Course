
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



