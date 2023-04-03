# Packing arguments
Or arguments parsing, `*args` and `**kwargs` can be very useful with creating 
new functions.

## *args
`*args` is a parameter, that will pack all the given arguments into a tuple.
While creating a function, we need to threat `*args` the same way as tuple - 
we cannot append any new values or delete them, however they are accessible for
outside functions. This is useful when creating a function that takes in a varying
amount of arguments.
```python
def my_mean(*args) -> float:
    return sum(*args) / len(*args)
```
This function will work, no matter if we input 2, 5 or 1000 values.

`*args` will work on all types of data, but we need to construct the function
carefully. We can also call args something else - most important is, that we
put the `*` before it.
```python
def greet_all(*names):
    for name in names:
        print(f'Hello, {name}!')
```
## **kwargs
`**kwargs` is another packing arguments, which intakes as many values as we give
it, but this time in form of a dictionary. It is useful for functions that use 
keyword arguments. There are a few ways for that, depending what we want to
achieve. Similar as with `*args`, `**kwargs` don't have to be named kwargs,
but the `**` are important.
```python
def hello(**person):
    #print(f"Hello, {person.name} {person.surname}.") <- one way if we want just a part
    print("Hello, ", end=" ")
    for key,value in person.items():
        print(value, end=" ")

hello(title = 'Ms.', name = 'Miła')
```

More resourses: [W3School](https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp),
[PythonTips](https://book.pythontips.com/en/latest/args_and_kwargs.html)