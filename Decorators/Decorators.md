# Decorators
Decorators are usually the functions we define to make our program prettier and
more functional. In Python, a decorator is a design pattern that allows you 
to modify the functionality of a function by wrapping it in another function.
The outer function is called the decorator, which takes the original 
function as an argument and returns a modified version of it.

We can distinguish a few different algorithms for functions, depending on 
the decorated function's arguments.

### For functions that do not have any arguments
```python
def lines_decor(func):
    def wrapper():
        print(f"---------------------")
        func()
        print(f"---------------------")
    return wrapper

@lines_decor
def hello() -> None:
    print('Hello!')

hello()
```
### For functions that take arguments
```python
def trigger_info(func):
    def wrapper(a, b):
        print(f"You have called for {func} with {a} and {b}")
        print(func(a, b))
    return wrapper

@trigger_info
def my_add(a: float, b: float) -> float:
    return a + b
```

Within the wrapper() and later func() we can either put the arguments or 
we can use `*args, **kwargs`, if we would like to make the decorator more universal,
for many functions that take in different values.
```python
def trigger_info(func):
    def wrapper(*args, **kwargs):
        print(f"You have called for {func}.")
        print(func(*args, **kwargs))
    return wrapper


@trigger_info
def my_add(a: float, b: float) -> float:
    return a + b

@trigger_info
def hello(name) -> str:
    return f"Hello, {name}!"
```

We can also distinguish a property decorator, which is used for encapsulation
in OOP. This has been explained in OOP notes.

More resources:
[DataCamp](https://www.datacamp.com/tutorial/decorators-python),
[RealPython](https://realpython.com/primer-on-python-decorators/),
[Programiz](https://www.programiz.com/python-programming/decorator),
[YouTube](https://www.youtube.com/watch?v=iZZtEJjQLjQ)