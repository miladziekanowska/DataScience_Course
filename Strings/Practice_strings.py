# Task 1
# Write a function which will return the reverse index of the given text:
# Input argumenst: string and index from the given string

def minus_index(words, index):
    if  0 <= index <= (len(words) - 1):
        return index - len(words)
    else: return -999


print(minus_index("bubble gum", 2))
print(minus_index("Good morning", 4))



