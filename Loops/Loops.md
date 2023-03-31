# Loops
Loops (repeated steps) have iteration variables that change each time 
through a loop.  - this is a syntax that allow to loop through sequence of 
values (usually a range, data structure or even strings) and it answers the 
conditions is true or false and applies our settlements and repeat the steps 
all over again for all the values we chose.

## While loops
The while loops are also called infinite. That means that as long as the 
condition is true, the loop will continue. It is essential to carefully 
construct the while loops, as if the condition shall always turn out true, 
the loop will continue on and on (that’s why these are infinite). 

```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)
```
Since all values except 0 are considered as *True*, the loop will continue 
until the n becomes 0. 

While loops are more dangerous than for loops and more prone to errors, if 
wrongly constructed. When creating a while loop, it's important to specify how
the variable will be changing, so ultimately reach a *False* input and the loop
stops.

Especially in while loops it is good practice to use break instruction 
(more on that in a bit) to make sure it stops at some value.

## For loops
For loops are also called definite loops, as they are being executed an 
exact number of times. They quite often consist of a list of items or a 
range, so a finite set of values. The loop can be written so it runs the 
oop once for each of the item. We say definite loops iterate through the 
members of a set.
```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")
```
For loops are more commonly used, as they are safer and most often we are
performing operations for finite number of elements. These are used, among others, for:
- looping through data structures;
- appending values to lists, sets and dictionaries;
- looping through strings and files;
- using the indexes in data structures
We can use *while* loops for some of these as well, but they are less likely to be used.

## Interrupting the loop
We have three keywords, which will allow us to interrupt the loop.
### break
The *break* allows us to break, finish the loop then a condition is met. 
The loop will no longer iterate.
```python
n = 0
while n < 10:
    print(n)
    n += 1
    if n == 6:
        break
```

### continue
The *continue* which will stop the current iteration and continue with 
the next (skips the element and continue until condition is true)
(it says “stop here, go back up”).
```python
n = 0
while n < 10:
    print(n)
    n += 1
    if n == 6:
        continue
    print("---")
```
### else
Similarly as with conditional statements, this will be executed at the end of
the loop, when the condition is no longer true.
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## Nested loops
We can write another loop within our loop. This is often used when dealing with
nested data structures, Numpy arrays, and also when looping through data structure
and letters.
```python
words = ["Apple", "Monkey", "Car"]
for word in words:
    for i in range(len(word)):
        print(word[i])
    print("---")
```

## range()
Commonly used with loops is `range()` function. It is especially important
if we need to loop through lists or strings and need numeric values and not letters,
for example for positioning. Such one example is above.

When it comes to structure:
`range(start, end, steps)` where the end is up to but not included.
However if we use it on a string or a list, it will return to the last position.
