#najlepsza forma importu
from math import sqrt
#unikamy importowania całych bibliotek przez import math albo *, dla czytelności i pamięci

#aliasowanie i importowanie własnych skryptów

from figures.flat import *
# staramy się nie tworzyc modułów bez korzystywania innych modułów
print(sqrt(4))

print(rectangle_area(4,5))
print(rectangle_circuit(3,4))
print(is_square(5,5))