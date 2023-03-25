# Task 1
# Create variables x and y and assing any numbers to them.
# Next, print all the prossible arithmetic operations using these variables

x = 4
y = 5

print("Addition: ", x + y,
      "\nSubtraction: ", x - y,
      "\nMultiplication: ", x * y,
      "\nDivision: ", x / y,
      "\nExponentiation: ", x ** y,
      "\nFloor division: ", x // y,
      "\nModulus: ", x % y)


# Task 2
# Write a string variable and then add any text to it.

string = "Ala ma kota, "
string += "kot ma pierdolca"
print(string)


# Task 3
# Write a program, whic takes input from the user with two float variables
# Then, print the sum, difference and product of these

value1 = float(input("Input first value: "))
value2 = float(input("Input second value: "))

print("Sum: ", value1 + value2,
      "\nDifference: ", value1 - value2,
      "\nProduct: ", value1 * value2)


# Task 4
# Write a program, which takes the input from the user with sting as "product name"
# and then the quantity of the product. Then print the gained information in format:
# product - quantity

product = input("Input the name of the product: ")
quantity = input("Input quantity: ")
print(product, " - ", quantity)
