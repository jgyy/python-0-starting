# Training Piscine Python for datascience - 0 Starting

**Summary:** Today, you will learn about the basics of the Python Programming Language.

**Version:** 1.1

## Contents

1. [General rules](#general-rules)
2. [Exercise 00](#exercise-00)
3. [Exercise 01](#exercise-01)
4. [Exercise 02](#exercise-02)
5. [Exercise 03](#exercise-03)
6. [Exercise 04](#exercise-04)
7. [Additional rules](#additional-rules)
8. [Exercise 05](#exercise-05)
9. [Exercise 06](#exercise-06)
10. [Exercise 07](#exercise-07)
11. [Exercise 08](#exercise-08)
12. [Exercise 09](#exercise-09)
13. [Submission and peer-evaluation](#submission-and-peer-evaluation)

## General rules

- Render your modules from a computer in the cluster using a virtual machine or directly on the computer.
- Your functions should not quit unexpectedly.
- Create test programs for your project (optional).
- Submit your work to your assigned git repository.
- Use Python 3.10 version.
- Use explicit lib imports.
- No global variables.
- Use your brain!

## Exercise 00

**Turn-in directory:** ex00/
**Files to turn in:** Hello.py
**Allowed functions:** None

Modify the string of each data object to display specific greetings.

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Expected output:
```
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

## Exercise 01

**Turn-in directory:** ex01/
**Files to turn in:** format_ft_time.py
**Allowed functions:** time, datetime or any other library that allows to receive the date

Write a script that formats dates in a specific way.

Expected output:
```
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

## Exercise 02

**Turn-in directory:** ex02/
**Files to turn in:** find_ft_type.py
**Allowed functions:** None

Write a function that prints object types and returns 42.

```python
def all_thing_is_obj(object: any) -> int:
    #your code here
```

## Exercise 03

**Turn-in directory:** ex03/
**Files to turn in:** NULL_not_found.py
**Allowed functions:** None

Write a function that prints the object type of all types of "Null".

```python
def NULL_not_found(object: any) -> int:
    #your code here
```

## Exercise 04

**Turn-in directory:** ex04/
**Files to turn in:** whatis.py
**Allowed functions:** sys or any other library that allows to receive the args

Create a script that takes a number as an argument and checks whether it is odd or even.

## Additional rules

- No code in the global scope. Use functions!
- Each program must have its main.
- Handle exceptions.
- All functions must have documentation (__doc__).
- Code must be at the norm (use flake8).

## Exercise 05

**Turn-in directory:** ex05/
**Files to turn in:** building.py
**Allowed functions:** sys or any other library that allows to receive the args

Create a program that takes a single string argument and displays the sums of its characters.

## Exercise 06

**Turn-in directory:** ex06/
**Files to turn in:** ft_filter.py, filterstring.py
**Allowed functions:** sys or any other library that allows to receive the args

Part 1: Recode filter function
Part 2: Create a program that filters words based on length

## Exercise 07

**Turn-in directory:** ex07/
**Files to turn in:** sos.py
**Allowed functions:** sys or any other library that allows to receive the args

Make a program that encodes a string into Morse Code.

## Exercise 08

**Turn-in directory:** ex08/
**Files to turn in:** Loading.py
**Allowed functions:** None

Create a function called ft_tqdm that copies the function tqdm with the yield operator.

## Exercise 09

**Turn-in directory:** ex09/
**Files to turn in:** *.py, *.txt, *.toml, README.md, LICENSE
**Allowed functions:** PyPI or any library for creation package

Create your first package in Python.

## Submission and peer-evaluation

Turn in your assignment in your Git repository. Only the work inside your repository will be evaluated during the defense.
