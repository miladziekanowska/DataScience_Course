# Function
---
A function is a reusable block of code. 
The brackets () after the name of the function are there to invoke it.
There are quite a lot of build-in functions in Python and even 
more in modules and libraries.
More on these later or along side different topics.

### Defining functions
When writing a program, there might be some chunks of code that will 
be repeated thorough the program.
Or perhaps we need one short automation which will save us some time, 
or perhaps we are writing a module.

In such cases it will be best to create a new function for this chunk 
of code and reuse it as many times as needed.
```python
def add(a: float, b: float) -> float:
    result = a + b
    return result
```
In the functions we can define the arguments with their expected 
types and we can also specify the expected data type of the result.
After that we put our code - whatever we want the function to do. 
Then we get to the `return`. To finalize the function, 
we need to know what exactly needs to be done when the function 
is called for.
- if we want the function to do some computation, but not return anything when it's called or printed, we do not use the return in defining function;
- if we want the function to do some computation and receive some output from it when the function is being printed - we use `return`;
- if we want the function to do some computation and once called print some output, instead of return, we can use `print()` within the function

**Best practice when creating functions:**
- use lower case to name the function;
- keep the function name as short as possible;
- use descriptive or mnemonic names;
- have fewer than 4 arguments (if there are 4 and more arguments needed, it's best to use class object instead);
- avoid duplicates;
- avoid input() within the function (if input data should be used, it needs to be outside of the function);
- the function should do one task;
- contain code with same level of abstract

### Arguments in functions and functions with no argument
We can create functions with no arguments in the the brackets,
when the functions has to deal with global variables, which are named
in the code within the function. The function will then only work with
the pre-defined global variables and unless we change the function,
no other variables or values can be used. This is however not a good practice.
This might lead to hard to find bugs.

We can also set a default or optional arguments for our function.
```python
def add(a: float, b = 1) -> float:
    result = a + b
    return result
```
By assigning the value of 1 to b, the function will not cause an error
when we input only one value when calling it. This is useful when we assign
some boolean arguments which might call for different outputs, depending
on their value. Default parameters need to be the last ones to be called
and cannot be followed by required input data.

## Generator object
Generator objects are slightly more advanced topic.
These will help with the optimization of code and will come in handy
when dealing with greater amounts of data. To avoid the memory, we can
`yield` each piece of data at one time and go to the next one. 
Only one piece of data is saved at the time in memory, instead of all.
Then if we use the function on our data (list, tuple, set, dictionary, file, etc.),
we will create the generator object.

```python
def row_call(names: list):
    for name in names:
        yield f"My name is {name}"

cheer = row_call(["Lola", "Lucy", "Maria", "Timmy"])

# if we print(cheer), it will give us information that this is a generator object
# if we want the generator object to work properly, after calling it, we need to loop through it

for name in cheer:
    print(name)
```
It is important to loop through the generator object. 
We could also print for each item in the data, however that wouldn't be
optimized to our liking and not as clear. Also when dealing with large
quantities of data, we do not know how many times this should be invoked.

More resources:
- [Real Python YT](https://www.youtube.com/watch?v=slX7bDwJ784)
- [Toward Data Science](https://towardsdatascience.com/12-of-my-favorite-python-practices-for-better-functions-7a21d18cfb38)
- [Digital Ocean](https://www.digitalocean.com/community/tutorials/python-return-statement)
