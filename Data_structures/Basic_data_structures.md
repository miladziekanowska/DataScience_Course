# Basic data structures
## Lists
Lists are the simples data structures, they are slightly similar to strings, 
since they share many methods, but are totally different in the sense of structure.
Most of our variables have one value in them - when we put a 
new value in the variable, the old one is overwritten.
A list allows us to put many values in a single *variable*. 
A list is nice because we can carry all many values around in one 
convenient package.
Also, a list is ordered and the order can be changed with methods. Lists are also mutable -
we can edit them at any given point. Therefore differently than with lists, using
methods on the list **will** impact them.

The indicator for list is a square bracket.
```python
friends = ["Sally", "Emma", "Thomas"]
jewelery = [ 1, 9, 12]
temperature = [4, -1.5, "cold"]
good_days = [5, [9,10,11], 26]
boyfriends = []
pets = list()
```
Lists are very conviniet - they store any type of data, in any quantity.
They can even store other lists *(nestet lists)* within them (or sets, or tuples, rather not dictionaries).
Just like strings, they go through methods and similar functions, but instead
of counting every symbol in the list, the positioning will indicate the position
of a value, however long or short it shall be.
```python
friends = ["Sally", "Emma", "Thomas"]
print(friends[0]) #This will print the first position, which is Sally
print(friends[0][0]) #This will print the first position of first position, which is S
```
Calling for positions within the values is from a concept of multiple dimentions,
which will come in handy when dealing with Numpy and other liblaries.

Lists, also similarly to strings, can be looped through (positioning works differently),
and concatenated using "**+**". They can also be sliced. 
### Lists methods
Some of the methods already included in Python for lists are:  
**list.append()** -> adds to an empty list  
**list.count()** -> looks for certain values in a list  
**list.extend()** -> adds things to the end of the list  
**list.index()** -> looks things up in a list  
**list.insert()** -> allows the list to be expanded in the middle  
**list.pop()** -> removes an item within the given index and stores it
**list.remove()** -> removes an item in the middle  
**list.reverse()** -> flips the order of the list  
**list.sort()**-> sort the list from smallest to largest (for descending: `.sort(reverse=True)`)

The `.pop()` is an interesting method and good to use if we want to store the
removed values. Best practice is to create a separate list using pop() method, 
if we plan on using them later. The `.remove()` will delete the value we want 
completely from the memory of the list.

### Temporal variable
Two flip the contact of two lists the most streamline way is to use a third variable to temporarily store one of the old values. e.g.:
```python
tmp = a
a = b
b = tmp
```
If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:
`a, b=b, a`

### Turning strings into lists
In many cases, we will turn strings into lists (or other data structures in general).
This will be very useful when dealing with files, since all files are being read as strings.
```python
abc = "With three words"
stuff = abc.split()
#here we turn a string into a list
print(stuff)
for w in stuff:
    print(w)
#here we spilt the list into separate words
```
When we don’t specify a delimiter, spaces will be treated like one delimiter. 
We can specify what delimiter character to use in the splitting. 
Useful, especially with csv tables, where we decide the delimiter.

### List comprehension
List comprehension is a very pythonic way of creating a list with fewer syntax.
The general syntax will look as following:
```python
list = [expression for item in iterable]
```
Using list comprehension all the values in within the list would have something
in common, since they are all iterated in the same way. 

List comprehension can also mimic some lambda function and be easier to read,
for example for filtering.
```python
list = [expression for item in iterable if condition]
```
If we want to add the **else** after the if condition, then we need to change the order:
```python
list = [expression if condition else ifelse for item in iterable]
```
### zip()
Another separate function to mention when dealing with lists is the `set()` function.
It allows us to kind of merge two lists together, as long as they have the same length (if they have different lengths, the length of the shorter one will be taken into consideration).
```python
spiecies = ["cat", "dog", "fish"]
names = ["Cloud", "Stan", "Bobby"]
pets = list(zip(spiecies, names))
```
The output of this operation will be a list of tuples.
## Sets
Sets are another data structure, very similar to lists, but with some critical
differences, which will determine if we are using a list or a set.

| Lists | Sets                                  |
| --- |---------------------------------------|
| Have and ordered structure | Are unordered (positioning won't work) |
| Values can have duplicates | Values have to be unique              |
| Open with square brackets | Open with curly brackets              |
| Can be created using empty bracets | Needs to be invoked with `set()` |

Turning a list into a set is a common practice to remove any duplicate values.
```python
colors = ["Blue", "White", "Green", "Blue", "Black"]
unique_colors = set(colors)
```
Due to the lack of order, most of the methods run on lists won't work on sets. 
The methods for sets:  
**set.add()** -> adds the given value to the set  
**set.update()** -> adds values from another set (or list or tuple) to the set  
**set.remove()** -> removes the given value from the set (given the value, not the position)  
**set.clear()** -> removes all the values from the set

## Tuples
Tuples are another data structure similar to lists.The biggest 
difference between tuples and lines is that they are immutable, so we 
cannot alter them. Once they are created, we cannot add to them or edit 
the inside. This way they take up less storage, are quicker to access and 
more efficient.
```python
a_tuple = (1, 4, 6, "me")
```
Since tuples structure is not modifiable, they are simpler and more 
efficient in terms of the memory use and performance than lists. Our 
program when we are making „temporary variables” we prefer tuples over lists.

Tuples are represented in normal brackets (). Since the tuples are immutable,
it is impossible to create an empty tuple and append to it. Therefore all the
modifying list methods won't work on tuples, but we can call the positions here.

## Dictionaries

Dictionaries use something that is called associative array.
They are Python’s most powerful data collection. Dictionaries allow us 
to do fast database-like operations in Python.

Differently than the above mentioned data structures, dictionaries let us find the
positions of the items, but differently than with lists and tuples, in dictionaries
the item are not ordered and rather called by their **key** than the numeric position.

Dictionaries are created within curly brackets {}.
```python
dictionary = {
    "Mike" : 98,
    "Harry" : 40,
    "Judy" : 55
} #this can be also represented in one line, but its more readable this way

#OR

phone_book = dict("Larry" = 486293453, "Suzan" = 294856300, "Louise" = 394586023)
```
In case of the above dictionary, the names represent the keys (keys are string values)
and the numbers are the values of the dictionary. 
### Dictionary methods
We have a few methods to check keys and values:  
**dictionary.keys()** -> returns all the keys in the dictionary as a list  
**dictionary.values()** -> returns all the values in the dictionary as a list  
**dictionary.items()** -> returns all the keys and their values in dictionaty as a list of tuples (key, value)

The keys cannot have duplicates while the values can have as many duplicates as desired.
And while keys are strings (it's not a good practice to make them int or float)
the values can be any data type.

Other useful methods for dictionaries would be:  
**dictionary.get("key")** -> will provide the value assigned to the key (if the key is not found, it will return None)  
**dictionary.update({"key" : "value"})** -> will append the key value in the dictionary  or update the existing pair  
**dictionary.pop("key")** -> will remove the key and value from the dictionary and store the removed value (only value!)  
**dictionary.popitem()** -> will remove last item that was inserted from the dictionary and store the key value tuple  
**dictionary.clear()** -> will clear the whole dictionary  

Instead of appending new values with `.update()` or updating existing value,
we can also use the following syntax:  
`dictionary["key"] = value`  
Similarly, if we want to delete an item (this doesn't remember the deleted value):  
`del dictionary["key"] = value`  
### Looping through dictionaries
Similarly to all data structures we can loop through the dictionary.
For that we usually use the methods related to the keys and values. 
While looping through only keys and only values works similarly as with lists or strings,
when looping through the items, the structure of the loop will be slightly different:
```python
for key, value in dictionary.items():
    print(f"{key}: {value}")
```
If we would like to use a list or a tuple as a set of keys to create a new dictionary
we would have to create a loop which will assign value to our new keys. 
```python
spiecies = ["cat", "dog", "fish"]
names = ["Cloud", "Stan", "Bobby"]

animals_1 = {}
animals_2
for i in range(len(spiecies)):
    animals_1[spiecies[i]] = names[i]
#OR
animals_2[spiecies[i]] = animals = dict(zip(spiecies, names))
```
Instead of joining two lists, the values can be assigned differently as well,
using math or input.

## Nesting
We can talk about nested lists or nested anything when we have one data structure
appended within another one. When dealing with nested loops, we need to use the positioning as
many times as deep is the element. This will come in handy when dealing with 
Numpy Arrays.
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# we want to access 5
print(nested_list[1][1])
```