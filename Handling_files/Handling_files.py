# Znak nowej lini: \n
# W przypadku plików linia = tekst + \n
# read(n) = czyta n znaków
# readline(n) = czyta n znaków do \n włącznie (po odczytaniu \n kończy działanie)
# readlines() = zapisuje pobranie linie do listy. 1 element = 1 linia + \n jeżeli występuje


# Przykładowy problem - wyświetl imię i jego długość
# with open("names.txt", "r", encoding="utf-8") as file:
#     # Benefit open
#     for line in file:
#         tmp = line.replace('\n', '')
#         print(f"{tmp} - {len(tmp)}")


# Napisać program który zliczy ilość wystąpień każdego słowa
# z pliku o nazwie reduta.txt
words = {}
with open("reduta.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.replace("\n", "").split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1

print(words)


with open("surnames.txt", "w", encoding="utf-8") as file:
    file.write("Kowalski\n")
    file.write("Nowak\n")
    file.write("Brzechwa\n")
    file.writelines(("Malinowski\n", "Morawiecki\n", "Killer"))


from random import randint
print(randint(1, 49))

n = int(input("Podaj ilość losowań: "))

for l in range(n):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(f"{randint(1, 49)} ")

    with open("lotto.txt", "a", encoding="utf-8") as file:
        file.writelines(numbers)
        file.write("\n")

# Użytkownik podaje ilość losowań (n), a następnie program zapisuje
# do pliku n przykładowych wyników lotto
# * Pomijaj duplikaty w losowaniu
#
# Przykład: użytkownik podaje n = 2
# Wynik (zawartość pliku):
#
# 2 6 12 40 31 22
# 12 34 49 21 1 12

