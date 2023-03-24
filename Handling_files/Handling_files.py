# Example - display name and it's length from names.txt

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        tmp = line.replace('\n', '')
        print(f"{tmp} - {len(tmp)}")


# Example 2 - write a program that counts the appearance of each wors in file reduta.txt

words = {}
with open("reduta.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.replace("\n", "").split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1

print(words)


# Example = create a new file surnames.txt

with open("surnames.txt", "w", encoding="utf-8") as file:
    file.write("Kowalski\n")
    file.write("Nowak\n")
    file.write("Brzechwa\n")
    file.writelines(("Malinowski\n", "Morawiecki\n", "Killer"))


# Example - create a program which creates a file with possible lotto draws.
# The number of draws is determined by user.

from random import randint
print(randint(1, 49))

n = int(input("Input the number of draws: "))

for l in range(n):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(f"{randint(1, 49)} ")

    with open("lotto.txt", "a", encoding="utf-8") as file:
        file.writelines(numbers)
        file.write("\n")



