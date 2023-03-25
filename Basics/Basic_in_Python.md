# Variables in Python
---
Python consist of **variables**, **operators**, **constants** and **reserved words**, which together create sentences - code.

**Variables** are one of the key components of any programing language - it is a container for any value and behaves as the value it contains. Variables are subjects of processes and operations, functions and so on. All the variables in the program are created by the author - no variables are set in Python.

There are two different types of variables in Python, in the sense of their usage and location:

- **Local variable**: Any variable declared inside a function is known as Local variable and it’s accessibility remains inside that function only;
- **Global Variable**: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.

```python
value_1 = 5 #this is a global variable

def adding_6(value):
	addition = 6 #this is a local variable
	sum_after = value + addition
	return sum_after

print(value_1) #this will work greatly
print(addition) #errors here
```

### General rules and good practices

Every variable in a code needs to have a **unique name**.

It is best to name the variables with their purpose (be mnemonic), however to short and to long names are not good as well. Python does not understand what is being typed beside reserved words and variables with names **x**, **banana** or **bullets2850** will be treated the same, as long as they are used in the further computation. 

- For shortly named things, like values of time, simple object name, the name should be fine;
- For naming longer named things, like *time spent in traffic*, try to abbreviate, e.g.: *t_traffic*;
- All names should start with a letter (optionally underscore but depends on the situation);
- Using singular and plural should rather be avoided or better indicated

Python is **case sensitive**, therefore it’s best to not differentiate the variables by the case.

It is also best to avoid differentiating variables with numbers, especially for greater values of variables (it would slide as a local variable for a few variables).

For naming variables only Latin alphabet, digits and underscore is available.

### Constans

Constans are any values in the code that are have not an assigned variable name. For instance:

```python
x = 5
y = x + 1
```

In this case, **x** and **y** are variables, whereas **1** and **5** are the constans. Constans are used for the computations, in expressions, etc., but there are non-changeable.

Constant can be also the data  we assign to the variable. Variable at this time is named place in the memory and store data, which is later retrieved by using the variable’s name.

Main thing is, when a constant has a name assigned, the value should not be changing within the code (it might be changed if the whole constant changes, but not due to the computation).

Constants are usually defined on a module level and written in all capital letters with underscores separating words

### Reserved words

The reserved words cannot be used in Python to name any variable. They can obviously be used as a string data. 

The words are as follow:

false, class, return, is, finally, none, if, for, lambda, continue, rue, def, from, while, nonlocal, and, del, global, not, with, as, elif, try, or, yield, assert, else, import, pass, break, except, in, raise

<aside>
💡 Although Python is case sensitive, these words will be recognized no matter of the case.

</aside>

### Data types for variables

The most commonly used data types are **strings** (a series of characters), **integers** (whole numbers), **floats** (decimal numbers) and **bools** (boolean). There are also other data types, some of them also indicate data structures. 

When creating a variable, Python is able to interpret the variable type without inferring it in every case, as it follows few simple rules:

- String data types are always surrounded by single or double quotations marks **’’** or  **””** (single quotations are a bit more common);
- Numeric data types can be entered as they are;
- Boolean data types should be typed starting with capital letter, so **True** or **False** (Python will recognize these anyway, but this is a good coding practice) and no quotation marks should be applied here;
- Similarly, none data type should be started with capital letter, so **None**, but Python will recognize it anyway;
- For other data types it depends on the shape of brackets or prefixes.

**Full list of data types**

| Example | Name | Type |
| --- | --- | --- |
| x = "Hello World" | str | text |
| x = 20 | int | numeric |
| x = 20.5 | float | numeric |
| x = 1j | complex | numeric |
| x = True | bool | boolean |
| x = ["apple", "banana", "cherry"] | list | sequence |
| x = ("apple", "banana", "cherry") | tuple | sequence |
| x = range(6) | range | sequence |
| x = {"name" : "John", "age" : 36} | dict | map |
| x = {"apple", "banana", "cherry"} | set | set |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset | set |
| x = b"Hello" | bytes | binary |
| x = bytearray(5) | bytearray | binary |
| x = memoryview(bytes(5)) | memoryview | binary |
| x = None | NoneType | none |

### How to check, change and cast the data type

Knowing the data type is key to performing operations on them, as depending on the type, some of them will be possible and some not so much. For instance, we cannot perform any math on strings, while it can easily be done on numeric data types. 

To check the data type of a variable we use **type()** functions. To display it, like with many other functions, we need to pair it with **print()** function, which is one of the commonly used functions.

```python
variable = "Hello World"
print(type(variable)) 
```

Once knowing the data type of the variable, there can be different functions performed on them, which is covered in other notes. 

Sometimes, the data type needs to be changed to perform an operation. Then, depending on the outcome data type, we need to assimilate the odd one to the other.

```python
name = "Michael"
age = 47
print("My name is "+name+", and I am "+age)
#this will not work, as name is a string and age is an integer
print("My name is "+name+", and I am "+str(age))
#this version will work, as all the variables are string now
```

The code above could also go other way - the string variable, if containing any type of numeric value, could be then converted into numeric data type and applied in expressions. 

<aside>
💡 When using **input()** in the future, remember that all the input values are by default strings. To perform math and other operations on them, the data need to be converted.

</aside>

For changing the data type there are few way, all of which are called data type casting. The functions for each data type can be found below.

One of the casting ways is to change the data type at first, this is permanent (or until someone changes it):

```python
age = 50
age = str(age)
print("His age is "+age)
```

Another way is to cast in the final formula, where we need the change:

```python
age = 50
print("His age is "+str(age))
```

When dealing with input data, we can also cast the input values, so that once entered, these will be in the desired data type:

```python
print("Please enter your age")
age = int(input())
age_in_5 = age + 5
print("You will be " + str(age_in_5) + " in 5 years!")
```

There is also an automatic casting when dealing with integer and float data. If at least one floating data should be in the expression, the result of the expression will always be in float, regardless if the value is decimal or whole.

For changes to boolean data type, the rules are quite simple:

- when dealing with integers or floats, the bool value will always be *True* as long as the variable value ≠ 0
- when dealing with string value, the bool value will always be *True* as long as there is any text (including interpunction and whitespace) - this becomes useful when dealing with input

**Full list of casts for data types**

| Example | Data Type |
| --- | --- |
| x = str("Hello World") | str |
| x = int(20) | int |
| x = float(20.5) | float |
| x = complex(1j) | complex |
| x = list(("apple", "banana", "cherry")) | list |
| x = tuple(("apple", "banana", "cherry")) | tuple |
| x = range(6) | range |
| x = dict(name="John", age=36) | dict |
| x = set(("apple", "banana", "cherry")) | set |
| x = frozenset(("apple", "banana", "cherry")) | frozenset |
| x = bool(5) | bool |
| x = bytes(5) | bytes |
| x = bytearray(5) | bytearray |
| x = memoryview(bytes(5)) | memoryview |

## Input() function

`input(prompt)` allows any user who is using the code to submit their own data into the problem.

There are a few best practices for the `input()` function:
- the input by default will always be a string. If we would like to receive different data type, it's best to cast the input with the proper type and if we are doing operations later on with the given variable, it's best to test it for errors;
- when creating a new function, which should process data from an input, it's not advised to put the input in the definition of function - it's much better to place the input earlier and then use the input variable we already received;
- it's good to write the *prompt*, which will be displayed when we call for an input from the user;


## Other useful basic functions

`dir(n)` - will provide all available methods and atributes, depending on the data type (will also work well with modules and libraries)

`type(n)` - will provide the correct data type of the n variable (if it's not clear or needed)

`help(n)` - will provide all the available funtions to be used on the n type of variable (will also work with modules and libraries)

`print(n)` - will print n in console or in program

With print, there are a few possibilities to print multiple variables and informations in one print.
One of them is concatenation, the other is `.format()` method and the other is `f""`. 













