# Object Oriented Programming
Object-oriented programming (OOP) is a programming paradigm that uses objects -
instances of classes - to represent and manipulate data. In Python, 
classes are created using the class keyword, and objects are created by 
calling the class as if it were a function. OOP allows for the 
encapsulation of data and behavior, as well as inheritance and polymorphism.

More on object oriented programming in Python: [Python documentation](https://docs.python.org/3/tutorial/classes.html),
[RealPython](https://realpython.com/python3-object-oriented-programming/)

The idea behind OOP is to create an object, which will be a representation
of real life objects. We can assign attributes to it (it has, it is...) and
methods/actions (what does it do). 

To create an object, we will have to call upon a `class`. Class describes
what attributes and methods that our distinct type of object will have.
It can be created in the main program or in a separate module and then imported.
It depends on how big the class will be, if it's large and in charge - separate
module will be better. To import a class from a separate file:  
`from class_file_name import Class_Name`

Now onto creating the class:

```python
class Food:
    def __init__(self, name: str, type: str, weight: float):
        self.name = name
        self.type = type
        self.weight = weight
        self.available = True
        
    def out_of_stock(self):
        if self.available:
            self.available = True
        else:
            self.available = False 
```
Above we have created object type Food. With the `__init__` function, we have
set up the attributes of the object. Although __init__ assigns that and kind
of constructs the object, in Python **this is not a constructor**. 

The other function is an inside class function, which will only work with 
objects of this class (and child classes). To call upon it, we need to type it
like a method.

```python
f1 = Food("Tiramisu", "Dessert", 200)
f1.out_of_stock()

f1.name = "Panna Cotta" #<- this is how we can change any of the object atributes
```
Good practice:
- name of the class should always start with a capital letter to be distinct;
- if we are creating just the class container for future code, it's best to type in `pass`;

## Magic methods
Magic methods in Python are the special methods that start and end with the 
double underscores. They are also called dunder methods. Magic methods are 
not meant to be invoked directly by you, but the invocation happens 
internally from the class on a certain action.

We define what the magic function does within the class and then we can use
it outside of the function, either by typing them directly or using the connected
symbols.
```python
    def __len__(self):
        return len(self.name)
    #with this, when we call len(f1) we will receive the len of it's name

    def __add__(self, other):
        self.weight = self.weight + other
    #when we call f1 + 200 somethere, the weight will be raised by 200

    def __str__(self):
        return f"{self.name}, {self.type}, {self.weigth} g"
    #when we call for (print(str(f1)) we will received the above defined string
```
More on that: [TutorialsTeacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)

## Inheritance and Polimorphism
Within a class we can define so called *child* classes, which will inherit the
attributes and functions from the *parent* class. The magic functions can be 
overwritten within the child class, but will still perform correctly within
parent class. The succession of the attributes and functions of the parent class
is called **inheritance** and the fact, that we can overwrite parent's class
functions is called **polimorphism**.
```python
class Menu(Food):
    def __init__(self, name, type, weight, price: float):
        super().__init__(name, type, weight)
        #Instead of super() we can use:
        #Food.__init__(name, type, weight)
        self.price = price
        self.ordered = False

    def is_ordered(self):
        if self.ordered:
            self.ordered = False
        else:
            self.ordered = True


    def __str__(self):
        return f"{self.name}, {self.price} - {self.available}"
```
This way we have created a child class Menu. This will inherit the function
`out_of_stock()` from the Food class, but the `is_ordered()` will not work on
the Food class. The `super()` function will copy the settings from the parent 
class when we want to overwrite some functions to make it more suitable for 
the child class. By using the `super()` function, you do not have to use 
the name of the parent element, it will automatically inherit the methods 
and properties from its parent.

More on inheritance: [W3School](https://www.w3schools.com/python/python_inheritance.asp), 
[Programiz](https://www.programiz.com/python-programming/inheritance),
[RealPython](https://realpython.com/inheritance-composition-python/#whats-composition)

More on polimorphism: [Edureka](https://www.edureka.co/blog/polymorphism-in-python/),
[Programiz](https://www.programiz.com/python-programming/polymorphism)

## Encapsulation
Encapsulation (*in polish - kapsułowanie*) can also be called data hiding,
as it restricts the access to the class' attribute, with help from
the property decorator.

Let's take our `Food` class example and add calories to it. Since some people
might have an eating disorder and calories might trigger them, let's hide them.
```python
class Food:
    def __init__(self, name: str, type: str, weight: float, calories: int):
        self.name = name
        self.type = type
        self.weight = weigth
        self.available = True
        self.__calories = calories #<- Notice the '__' next to attribute name.
                                    # this tells us this attribute is encapsulated
```
With the encapsulation of calories, we are not able to access or change the
calories value like we could do with name or weight. With the '__' next to
the property name we have encapsulated this attribute. This is a so-called
**private attribute**. Now we need to know how to access it.

For that we will need to create two decorators: **getter** and **setter**.
As the names suggest, the getter allows us to get to the values, display them,
and setter allows us to set them.

Let's create them for the calories attribute.
```python
    #getter
    def calories(self):
        return self.__calories

    #setter
    def calories(self, new_calories):
        self.__calories = new_calories
```
The way it differs from calling `object_name.calories` in a print or update way
is that getter and setter access these data from within the class, and not from
the outside, from which it is protected.

It is a good practice to name getter and setter the same way we name the
attribute to work faster with our code, but these can be changed if it's required.

There are also protected attributes, which are accessible within the 
class and also available to its sub-classes. These are defined with "_"
in front od their name in the `__init__`. 

More about encapsulation: [PyNative](https://pynative.com/python-encapsulation/),
[GeeksForGeeks](https://www.geeksforgeeks.org/encapsulation-in-python/)