# Basics in Python
# Data types
txt = "Ala ma kota"
number = 12
num_with_precision = 9.99
true_or_false = True

print(type(txt))

# Printing to the console
print(10 + 9.99)
print("Value of variable txt is:", txt)

# Working with variables
num_a = 10
num_b = 5
print("The sum is:", num_a + num_b)
print("The difference is:", num_a - num_b)

# Text concateranion
animal = "a cat"
person = "Ala"
result = person + " has " + animal
print(result)

# Math operations
print("Exponentiation:", 2 ** 3)
print("Modulus:", 10 % 3)
print("Floor division", 100.0 // 3.0)

# Shortened version
result = 2
my_power = 10
result **= my_power
print(result)
# x = x [operator] [value] can be written as: x [operator]= x [value]

# User's input
first_name = input("Enter your name: ")
print("Hello,", first_name)
age = input("Enter your age: ")
print("You've entered:", age)

# Conversion
# Format: data type (digit/variable to convert)
# str(), int(), float(), bool()

num_a = int(input("Enter number: "))
print("Sum:", num_a + 10)
print("From float to intiger:", int(9.9999999))

# input()

# it is possible to receive multiple variables from one input

name, age, score = input("Enter student's name, age and score separated by space:").split()
print("Student Name:", name)
print("Student Age:", age)
print("Student Score:", score)

# miltiple input can also be put into a list

entered_list = input("Enter a list of numbers separated by space: ").split()

num_list = list(map(int,entered_list))
print('Number List: ',num_list)
print('List sum:', sum(num_list))


# input() can also be used in a loop, so that it will keep ask for data until the requirements are met
total_input = []

while True:
    name = input("Enter Student Names: ")
    if name:
        total_input.append(name)
    else:
        break

print('Total input received :')
print(total_input)