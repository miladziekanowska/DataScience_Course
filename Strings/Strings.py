#fprint rounding

value = 9.3566225
c = 300
print(f"Wartość: {value:6.2f}") #6 means the amount of symbols our change will take here (spaces, digits and dotsa
print(f"Wartość: {value:.2f}")
print(f"Wartość {c:4d}")

i = 10
print("My i is equal to:", i)
# f"" can also be used for creating variables from other variables
print(f"My i is equal to {i}, and 2^i is: {2 ** i}")
animal_count = 10
info = f"Ala has {animal_count} cats"
worse_info = "Ala has " + str(animal_count) + " kats"
print(info)


# fprint round (formatowanie)
value = 3.98777773
c = 200
print(f"Value: {value:6.2f}")
print(f"Value: {value:.2f}")
print(f"Value: {c:4d}")

# ---------------------------------------
print("--------------------------")
print(f"A: {100:10d}")
print(f"B: {2500:10d}")
print(f"C: {1000000000:10d}")
print("--------------------------")
