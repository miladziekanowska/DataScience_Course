# Strings in Python

A string it a sequence of characters and a data type other than 
integer and float. A string literal uses  quotation marks. 
In Python we can concatenate strings by using a +, however, 
if we concatenate two numbers, which are strings, it won’t be an 
addition but display of two numbers, e.g. “3”+”3” = 3, 3.

Inside a string, we can get at any single character in a string 
using an index specified in square brackets. The index value must 
be an integer and starts at zero. The index value can be an
expression that is computed.

| B | a | n | a | n | a |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 |
| -6 | -5 | -4 | -3 | -2 | -1 |
```python
fruit = "banana"
letter = fruit[1]
#or letter = fruit[-5]
```
Positioning in strings (and later in other data structures) is very useful
and can be used for different things, like looping through strings or slicing them.

With positioning, we can put it in simple structure:
`print(string_variable[X:Y, Z])`
where:  
- **X** is for the first position (if we leave it empty, by default it's 0)  
- **Y** is for the last position (if we leave it empty, by default it's last)  
- **Z** indicates the difference between each printed symbol (if we leave empty, by default it's 1, if we want to skip every second symbol, we can use 2, and if we want to go the reversed order: -1)
These can as well be indicated using e.g. `len()` method. However, we 
- cannot index beyond the length of the string, otherwise an error will occur.

### Looping through strings
Looping through strings will be another operation we will use frequently.
**For** loops are the preferred ones, but in some cases we will use **while**.
The iteration variable “iterates” through the sequence (ordered set). 
The block (body) of code is  executed once for each value in the sequence. 
The iteration variable moves through all of the values in the sequence.
This is also the place where we can differentiate and use local variables
with singular form, if the variable is multiple.
```python
fruit = "banana"
for x in fruit:
    print(x)
```
The **in** keyword can also be used to check to see if one string is “in” 
another string. The in expression is a logical expression that returns 
True or False and can be used in an if statement.
```python
fruit = "banana"
if "n" in fruit:
    print("Found it!")
```
Strings can be compared with each other, similarly to using `max()` and `min()` 
operators. It really depends on capital and small letters and the order 
in alphabet (e.g. a > b, a > A). It runs as far as it needs, does not 
compare all the values, just one is enough if there is a difference 
(not really useful unless sorting a pretty clean set of data). This comes down to 
the binary representation of these letters.

Another very useful function used with strings is `len()`.
Once used, it returns the lenght of the string (including spaces and punctuation).
The new line symbol *\n* is counted as one symbol, not two.

### String methods
Besides functions and loops, we can also used methods on strings.
Methods are written after the `string.HERE()` and can be compiled.
Using methods does not alter the variable - it temporarily alters it in the
context of the function or loop, etc. For example to avoid wrong sorting due to
upper and lower case letters (since they have different values in binary),
it's best to use either `.upper()` or `.lower()` method, so that all the letters
will be same size, therefore closer with values.

Some of the useful functions: (and these can be chained together!)
- **string.find(“x”)** - searching for a substring within another string (if the substring is not found it returns **-1**
- **string.upper()** - converts to upper case (it’s a copy, not change)
- **string.lower()** - converts to lower case (it’s a copy, not change)
- **string.replace(**“Searching string”,”Replacement string”**)** - searches and replaces substrings (it’s a copy, not change)
- **string.lstrip()** - removes front whitespace (left)
- **string.rstrip()** - removes back whitespace (right)
- **string.strip()** - removes all white spaces
- **string.startswith(“String”)** - finds if the line starts with particular letter/word/etc. (provides true or false)

Another cool option using methods would be checking if any of the symbols
within the string is, for example, a digit. 
```python
password = "pandas96"
string = any(map(str.isdigit, password))
```
This code can be used with any .is... () method. It will return boolean value.

### String formatting

This metod is created for Python above 2.6 version. 
It allow for the variable to be entered to text by using **{}**. 
The type of data can also be indicated in this:
- {:s} for string;
- {:d} for integer;
- {:f} for float.

```python
x = 1
y = 3.5
s = "brown"
print("I've got {} banana".format(x))
print("I've got {:s} banana".format(s))
print("I've got {:3.2f} banana".format(y))
```
💡 In the **{:A.Bf}** the A is for the amount of spaces in front of the variable, while the B is for the decimal places.

We can also use the **f""** string formatting while printing, which is
much easier and the curly brackets work similarly with positioning the print.