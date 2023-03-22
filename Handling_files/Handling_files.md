# Handling files

## Opening files
There are two ways of opening files. 
```
file = open(names.txt)
```
or
```
with open("reduta.txt", "r", encoding="utf-8") as file:
```

The second value after the mode in which we open the file, and the third is for encoding.
The default mode for opening files is "r", while the encoding is UTF-8 by default. 
There are also different types of modes:

| **Mode** | **Description**                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------|
| r        | Open a file for reading.                                                                                         |
| w        | Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.             |
| x        | Open a file for exclusive creation. If the file already exists, the operation fails.                             |
| a        | Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. |
| t        | Open in text mode. (default)                                                                                     
| b        | Open in binary mode.                                                                                             |
| +        | 	Open a file for updating (reading and writing)                                                                  |

Coming back to the possibilities with opening.

Both ways will work just fine when used correctly. However, the first
possibility will require additional syntax for closing file at the end, when we are done
with our exploration or modifications. 
In the `with open()` syntax, the file will be closed as soon as the loop or modifications
under the syntax are done, so it's much more optimized.

For reading a file, two functions are most common.
`read(n)`, where the n amount of characters from the file will be read (we do not have to specify the n),
and `readlines(n)`, which is similar, but returns all first n characters from each line (lines are separated by **\n**).

## Editing and creating files

The same way a file can be open, it can also be created, if there is no file with the same name in the directory.
Once the operations under the `with open()` syntax (or between `open()` and `close()`) are done, the file will be created automaticly.
For this, we mainly use **w** or **a** mode in the opening. The difference is, that when using a, we are appending whatever we write at the end of the file, while when using w, we can dictate the location of the add ins (by default it is also at the end of the file).

The most common commands to edit the files are:
`write(s)`, where the string s is written in the file and also returns the number of characters written;
`writelines(s)`, where a list of lines is written (commonly used with loops).