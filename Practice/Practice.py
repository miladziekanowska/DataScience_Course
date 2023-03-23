# Zadanie 01
# Napisz program który pozwoli wygenerować dowolną liczbę (wierszy) danych według poniższego schematu
# * godzina:minuta
# * wartość od 0 do 100
# * wartość od 0.1 do 1.0
# Każde wartości powinny być oddzielone średnikami
# czas;war1;war2
# W przypadku losowości wartości użyjecie randint oraz uniform (obie znajdują się w random)
# Natomiast godzina:minuta ma być również losowana
# (do funkcji timedelta wykorzystać randint)
#
# nazwa pliku:        dane_dzienmiesiacrok

from datetime import datetime as dt, timedelta as td
from random import randint, uniform

now = dt.now()
file_name = f"dane_{now.strftime('%Y%m%d')}.txt"

for _ in range(10):
    with open(file_name, "a", encoding="utf-8") as file:
        for _ in range(100):
            time = now - td(hours=randint(-24, 24), minutes=randint(-60, 60))
            # time = f"{randint(0,23):2d}:{randint(0,59):2d}".replace(" ", "0")
            first_value = str(randint(0, 100))
            second_value = str(round(uniform(0.1, 1.0), 2))
            row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
            file.write(row)


# Wykorzystując dane z ```Zadanie 01```:
#
#  Dodać nową kolumnę do pliku (można do nowego), która będzie wynikiem
#  operacji matematycznej: kol2 * kol3
#  operacji matematycznej: kol2 * kol3, natomiast pierwsza kolumna ma posiadać informacje tylko o godzinie.
#
#  Ostatecznie:
#
#  * Godzina
#  * war1 (0-100)
#  * war2 (0.1-1.0)
#  * war1 * war2


for _ in range(10):
    with open(file_name, "a", encoding="utf-8") as file:
        for _ in range(100):
            time = now - td(hours=randint(-24, 24), minutes=randint(-60, 60))
            # time = f"{randint(0,23):2d}:{randint(0,59):2d}".replace(" ", "0")
            first_value = str(randint(0, 100))
            second_value = str(round(uniform(0.1, 1.0), 2))
            row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + ";" (first_value + second_value)"\n"
            file.write(row)




ZADANIA ETL (extract, transport, load)