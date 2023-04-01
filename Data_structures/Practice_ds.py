# Task 1
# Create a function called add_contacts, which will intake following arguments:
#   - dictionary with contacts
#   - key name
#   - phone number (string).
# If the contact is in the dictionary, return that it already exists;
# If the contact is not in the dictionary, add it and confirm that.
# The function does not return anything.
#
def add_contact(contacts: dict, name: str, phone: str) -> None:
    if name not in contacts.keys():
        contacts[name] = phone
        print("Contact has been added!")
    else:
        print("This person is already in contacts!")


# Task 2
# Given the dictionary "data", create a new dictionary from these tuples where:
#   key = first value
#   value = second value / 50
# Program should skip all the duplicates.


data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]

dataset = {}

for i in range(len(data)):
    if data[i][0] not in dataset.keys():
        dataset[data[i][0]] = data[i][1] / 50

print(dataset)

# Task 3
# Write a function named manage_list, which intakes two arguments:
#     - command: add and delete;
#     - value
# If add is used, we add the value to the list, and if it's delete, it should
# be deleted using pop().
# The function does not return anything

def manage_list(command: string, value: int) -> None:
    if command == "add":
         list.append(value)
    elif command == "delete":
         list.pop(value)