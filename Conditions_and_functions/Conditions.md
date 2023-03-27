# *If* statements
---
Conditional instructions are commonly used for testing logical conditions.
`If` statements are one of teh most common way for this kind of testing.

```python
if condition1:
    #instruction if the condition1 is true
elif condition2:
    #instruction if condition1 is false, but condition 2 might be true
else:
    #instruction if all the conditions are false
```
The conditions must bring a boolean value when executed. The instruction can be as long as needed, as long as they are within same indentation.
For clear code, if the instructions are longer, is best to stick with the indented form.
For shorter conditions, the condition can be done in one short line:
```python
if a > b: print("a is greater than b")
```
If else structure can also be used while assigning values to variables or while printing, if we want a condition to determin the output.
These are so called **ternary operators**.
```python
is_nice = True
state = "nice" if is_nice else "not nice"
```

It's important to know, that the conditional instructions can be nested.

### Logical operators

Logical operators are used for logical expressions, where we want to receive boolean data, but also used in complex loops or conditions.

| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

### Identity operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

An operator **is** can be used in a logical expressions in Python. It implies “is the same as”. It is similar to, but stronger than **==**. **Is not** is also a logical operator. Besides the value, **is** also compares the data type. So 0 is 0.0 if false, since 0 is integer and 0.0 is a float. It is best to use **is** or **is not** only on boolean and none types of data.

| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |
| == | Returns True if both variables have the same value |  |
| ! = | Returns True if both variables have different value |  |

### Membership operators

Membership operators are used to test if a sequence is presented in an object - commonly used when dealing with strings or any data structures.

| Operator | Description | Example |
| --- | --- | --- |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

More resources:
- [Data camp](https://www.datacamp.com/tutorial/elif-statements-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19863514238&utm_adgroupid=147433231419&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=651936075018&utm_targetid=dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=1031024&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-in_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-marayc23&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY3CKxMCZN2P1RdU9zTCQTqEc5sBU-0iNUIBjmxa1QzBniikjMNXd5AaAnZmEALw_wcB)
- [W3schools](https://www.w3schools.com/python/python_conditions.asp)
- [Simplilearn](https://www.simplilearn.com/tutorials/python-tutorial/python-if-else-statement)
- [Programiz](https://www.programiz.com/python-programming/if-elif-else)