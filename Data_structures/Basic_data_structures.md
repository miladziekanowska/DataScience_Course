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
abc = "With thre words"
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

## Dictionaries