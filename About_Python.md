## What is Python?

Python is a scripting language. It uses English keywords. Whereas, other languages use punctuation, Python has fewer syntactic constructions.

Python is:
- **high-level** (queries are short and readable for mundanes and can be very powerful);
- **interpreted** (run through program line by line and execute each command directly from the source code, with no intermediary compilation step, but can be edited in one point, without the need to re-writing the code; Python can be executed as both but in most uses it’s interpreted);
- **interactive** (allows to make changes to the program while it is already running);
- **object-oriented** (uses the concept of objects, not procedures);
- **dynamically typed** (types of variables are automatically recognized);
- **cross-platform** (compatible with different environments, like Mac, Windows or Linux, etc.)
- **general purpose language** (can be used for many different things, like data analytics, data science, machine learning, games and apps, back- and frontend, automation, etc.)
- **free and open-sourced**;

## How is memory managed in Python?

Python is an interpreter based language that dynamically allocates memory using its **Memory Manager**. Although it takes away the liberty of managing the memory from the developer, it hands out some tools to make the code more robust and understandable.
Since there is no option for manual memory management, Python uses a built-in **Garbage Collector** that continuously looks for un-referenced objects and deletes them from memory. This ensures good optimization of memory at the cost of the speed of code execution.
**Heap space**  in Python primarily maintains all objects and data structures, whereas its counterpart, **stack space**, contains all the references to the objects in heap space.
When an object is updated, the new value is written at a new location and the variable is referenced to the new address. As soon as references to an object reach 00, the **Garbage Collector** wipes it from the heap. This is different from other languages like C++, where the value is updated at the same location.

