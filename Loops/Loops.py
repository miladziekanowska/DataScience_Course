# FOR loop
# with string:
for c in "KITTY":
    print("Letter:", c)

# For every word in a string
for word in "She has a cat".split(" "):
    print("Word:", word)

# For nested loops
accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 1999.97),
    ("A002", "600100", 62780.00)
]
for element in accounts:
    print("Client:", element)

# Using the range() function
for i in range(2, 10, 3):
    print("Number:", i)

# Descending row
for i in range(10, -1, -1):
    print(i)




# WHILE LOOP
n = 0
while n < 10:
    n += 1
    print(n ** 2)

txt = "she-has-a-cat"
n = 0

while n < len(txt):
     print(txt[n])
     n += 1