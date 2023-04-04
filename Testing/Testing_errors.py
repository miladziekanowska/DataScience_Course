def dec_to_bin(value: int) -> list:
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]


x = 10

try:
    print(x / 0)
except ZeroDivisionError:   # expect: <-- instructions for any error
    print("You have tried to divide by 0.")
finally:
    # Do it everytime at the end, no matter if there are any errors
    print("I'M DONE")

a = [10, 20, 3, 4, "She has a cat", True, 3, 4, 12, "Doggy", "XD", 20]
errors_value = []

for i in range(len(a)):
    try:
        a[i] = dec_to_bin(a[i])
    except TypeError:
        errors_value.append(a[i])




try:
    print(10 / 0)
    print("She has " + 5 + "cats.")
except ZeroDivisionError:
    print("Division by 0 detected")
except TypeError:
    print("There is an error with your data type")


# Example
# To our function add the try... except if the user provides an input that cannot be converted to int
try:
    n = int(input("Input a number: "))
    summary = 0

    while n >= 0:
        summary += n
        n = int(input("Input a number: "))

    print(f"The sum of your values is: {summary}")

except ValueError:
    print("Wrong input was given. Did you try to input anything containing letters?")





# Rozwiń funkcjonalność zadania z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontynuuj działanie
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)