# Task 1
# Write a function which takes in a string. The function returns a dictionary with following schema:
#     key - letter
#     value - how many letters are there

n = str(input("Wprowadź wyrażenie: "))

def letter_counter(word):
    letters = {}
    for i in word.lower():
        if i not in letters.keys():
            letters[i] = word.count(i)
    print(letters)

letter_counter(n)

# Task 2
# Write a program which given the users input (int) returns all even values from 0 to n (included)

number = int(input("Input your number: "))
a = 0
while a <= number:
    print(a)
    a += 2

# Task 3
# Using the while loop write a program which will diplay all roots from 10 to 2, descending

a = 10
while a in range(10, 1, -1):
    print (f"The square root for {a} is {a ** 0.5}.")
    a -= 1


# Task 4
# Write a program, which sums up all the integers from the given range. The user inputs the begining and end

start_value = int(input("Start value: "))
end_value = int(input("End value: "))
start_sum = 0

for b in range(start_value, end_value + 1):
     start_sum += b

print(start_sum)


# Task 5
# Using the given list of tuples, create a dictionary using the following schema:
#   key - first tuple value
#   value - second tuple value divided by 50
# If the key is already in the dictionary, it should be skipped

data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]

dictionary = {}

for person in range(len(data)):
    if data[person][0] not in dictionary.keys():
        dictionary[data[person][0]] = data[person][1] / 50
print(dictionary)

# Task 6
# Create a function which will recognize if a given wors is an izogram or not.

def izogram(word: str) -> bool:
    letters = set()
    for w in word.lower():
       if w in letters:
           return False
       letters.add(w)
    return True