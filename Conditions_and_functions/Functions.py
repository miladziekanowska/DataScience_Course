# Simple functions
def show_sum(a: int, b: int) -> int:
    print("Sum:", a + b, "Sum:", a + b)

def add(a: int, b: int) -> int:
    result = a + b
    return result


x = add(1, 9)
print(x)
print(add(99, 101))

# Generator object
def row_call(names: list):
    for name in names:
        yield f"My name is {name}"

cheer = row_call(["Lola", "Lucy", "Maria", "Timmy"])

for name in cheer:
    print(name)