# 1. Napisz funkcję o nazwie add_contacts, która przyjmuje następujące argumenty:
#     - słownik z kontaktami (dict)
#     - nazwę klucza (str)
#     - nr telefonu (str)
#     Następnie funkcja wypisuje na konsoli komunikat:
#     - kontakt dodanom jeśli dodaliśmy kontakt,
#     - kontakt istnieje, jeśli podany klucz istnieje w słowniku
#     Funkcja niczenie nie zwraca

# 1.

 def add_contact(contacts, name, phone):
     if name not in contacts.name():
         contacts[name] = phone
         print("Kontakt dodano.")
    else: print("Kontakt istnieje.")