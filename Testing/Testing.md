## Testing errors

Testing errors allows us to set a kind of warning in the code, where we might expect an error to happen.
With the testing, we are aware of possible errors, so we set a detour around them, so even if they happen, the further code can run smoothly.
```
try:
	x = float(“Hello”)
except:
	x = (-1)
```

This way if we receive an error, the program won't stop running, 
but will provide us with the designated value or print for this occasion.

In addition to the `try except`, we have two additional commands:
- `finally`, which we use at the end of the testing, if we want to
- `quit()`, which we can use after an except, to close the tested part

### Most common exceptions:
- *TypeError* – incorrect data type has been used
- *KeyError* – key in dict cannot be found
- *IndexError* – wrong index has been called
- *ModuleNotFoundError* – imported module cannot be found
- *AssertionError* – assert in testing cannot be successfully run
- *NameError* – object cannot be found (usually typos)
- *SyntaxError* – wrong syntax (also usually typos)
- *ZeroDivisionError* – dividing by 0

### Good practice

- Instead of writing dry `except:`, it's best to figure our common errors for our function or loop (wherever we want to implement testing) and create an except for individual errors. The empty `except:` should only be used at the end, if there is a danger of an error outside our knowledge, to further secure the code.
- We can create a list of all the errors that happen and check it later to further improve our code

More resources:
- [W3School](https://www.w3schools.com/python/python_try_except.asp)
- [Python documentation](https://docs.python.org/3/tutorial/errors.html)
- [Geek4Geeks](https://www.geeksforgeeks.org/python-try-except/)

## Testing code

Software testing is part of the quality assurance process. Testing verifies the correctness of the created software and validates whether a given system meets the client's needs. Most often associated directly with the profession of a tester, however, it is performed during the entire software development process.


More resources:
- [RealPython](https://realpython.com/python-testing/)
- [Python documentation on unittest](https://docs.python.org/3/library/unittest.html)
- [Freecodecamp](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/)
- [Ideo (PL)](https://www.ideo.pl/firma/o-nas/nasze-publikacje/testowanie-manualne-i-automatyczne,167.html#:~:text=Testy%20automatyczne%20należy%20najpierw%20opracować,końca%2C%20opracowania%20raportu%20lub%20podsumowania)

*In works*
