# 1. Napisz funkcję o nazwie add_contacts, która przyjmuje następujące argumenty:
#     - słownik z kontaktami (dict)
#     - nazwę klucza (str)
#     - nr telefonu (str)
#     Następnie funkcja wypisuje na konsoli komunikat:
#     - kontakt dodanom jeśli dodaliśmy kontakt,
#     - kontakt istnieje, jeśli podany klucz istnieje w słowniku
#     Funkcja niczenie nie zwraca

# 1.

 # def add_contact(contacts: dict, name: str, phone: str):
 #     if name not in contacts.name():
 #         contacts[name] = phone
 #         print("Kontakt dodano.")
 #    else: print("Kontakt istnieje.")



# Mamy listę danych:
data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]
#
# Należy przepisać powyższe krotki do słownika danych według poniższego schematu:
#     klucz - 1 wartość krotki
#     wartość - 2 wartość krotki podzielona przez 50
#
#     Przykładowo dla pierwsze elementu listy powinnyśmy otrzymać wpis:
#     "Adam": 15
#
#     Program ma pomijać klucze które są duplikowane (wchodzi pierwsze wystąpienie),
#     czyli drugi "Adam" powinien być pominięty w przetwarzaniu.


#
# dataset = {}
# for i in range(len(data)):
#
#
# for value in dataset:
#     value = value / 50
#
# print(dataset)



# 4. Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca

#4.
def manage_list(command, value):
    if command == "dodaj":
         list.append(value)
    elif command == "usun":
         list.pop()