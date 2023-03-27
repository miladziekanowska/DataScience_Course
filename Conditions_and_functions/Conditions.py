# Arithmetic condition
cost = 3.10
product = "onion"

if cost >= 3:
    print("Don't buy, it's expensive!")
else:
    print("Buy, it's cheap!")

# Operators: not, and, or
if product == "onion" and cost < 3:
    print("Buy the onion!")
else:
    print("Don't buy the onion, it's to expensive!")

# Case study: Grades within range 2.0 do 5.0

grade = 5.2

if 2 <= grade <= 5:
    print("Correct grade!")
else:
    print("Incorrect grade!")

# elif
cost = 2.99
product = "carrot"

if product == "onion" and cost <= 3:
    print("Buy the onion")
elif product == "carrot" and cost <= 4.5:
    print("Buy the carrot")
elif product == "vodka" and cost <= 19.99:
    print("You buy alcohol")
else:
    print("Don't buy anything!")
