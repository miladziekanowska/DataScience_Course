# Task 1
# Given the user's input, provide the information if the number is even or odd.

number = int(input("Input the number: "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# Task 2
# Given the user's intiger input, write a program, which:
#    Will display "Piff paff" if the intiger is divisible by 3 and 5,
#    Will display "Piff" if the intiger is dividible only by 3,
#    Will display "Paff" if the intiger is diidible only by 5,
#    Will display "Your number is:" + input, if no conditions are met.

entry = int(input("Input a number: "))
if entry % 3 == 0 and entry % 5 == 0:
    print("Piff Paff")
elif entry % 3 == 0:
    print("Piff")
elif entry % 5 == 0:
    print("Paff")
else:
    print("Your number is ", entry)

#  Task 3
#  Create a new function is_even, which take an argument and returns True if the number is even,
#  and False if the number is odd. With the new function, return the information if it's even or odd.

value = int(input("Input a number: "))

def is_even(x):
      return x % 2 == 0

if is_even(value):
    print("Even.")
else:
    print("Odd.")

# Task 4
# Write a function my_pow, which will return the exponentiation of the given number.

val = int(input("Input the number: "))
power = int(input("Input the power: "))

def my_pow(val, power):
      return val ** power



# Task 5
# Program receives two inputs:
#    1. Quantity of correct answers (int)
#    2. Quantity od questions (int)
# Then the program displays the correct note for the % as follows:
#    100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
#    69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0

answers = int(input("Input the quantity of correct answers: "))
questions = int(input("Input the quantity of questions: "))
percentage = answers / questions * 100

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

# Task 6
# Write a function named show_temp_status, which receives one float argument.
# Then it returns a string depending on the value of an argument:
#     Below 36.4 - Hypothermia
#     <36.4 36.8> - Norm
#     (36.8, 37.0> - Low-grade fever
#     Above 3.71 - Fever

def show_tem_status(temp):
    if temp < 36.4:
        return "Hypothermia"
    elif temp >= 36.4 and temp <= 36.8:
        return "Norm"
    elif temp > 36.8 and temp <= 37.0:
        return "Low-grade fever"
    else:
        return "Fever"

