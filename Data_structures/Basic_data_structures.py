numbs = [1,4,6,2,8,0.5,"a", 1]
n = set(numbs)
print(n)

# list comprehension

squares = []
for s in range(1, 11):
    squares.append(s * s)
# we can get the same result this way:
square = [s * s for s in range(1, 11)]

print(square)
print(squares)

# filtering with list comprehension

score = [100, 36, 90, 63, 84]
passing = [s for s in score if s > 50]
print(passing)

# dictionary

dictionary = {
    "Mike" : 98,
    "Harry" : 40,
    "Judy" : 55
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

removed = dictionary.pop("Mike")
t = dictionary.popitem()

fella = (4,6,7,8,2)

spiecies = ["cat", "dog", "fish"]
names = ["Cloud", "Stan", "Bobby"]
pets = list(zip(spiecies, names))
print(pets)

animals = dict(zip(spiecies, names))


animal = {}
for i in range(len(spiecies)):
    animal[spiecies[i]] = "1"

print(animal)

counts={"me" : 1, "you" : 5, "us" : 29}
for key in counts:
    print(key, counts[key])