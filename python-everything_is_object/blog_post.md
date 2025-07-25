# Understanding Mutable and Immutable Objects in Python

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## Introduction

In this blog post, I will explain some core Python concepts that every developer should understand. These include the difference between mutable and immutable objects, how Python handles variables internally, and how arguments are passed to functions. These concepts can influence how your code behaves, especially when dealing with functions, data structures, and memory management.

## Id and type

In Python, every object has an **identity** and a **type**. The identity is a unique identifier for the object (usually its memory address), which can be accessed using the `id()` function. The `type()` function tells you the kind of object you're working with.

```python
x = 10
print(type(x))  # <class 'int'>
print(id(x))    # e.g., 140732323856784

x = 11
print(id(x))    # Different from before – new object

```

## Mutable Objects
Mutable objects can be changed after they are created. This means their content or internal state can be modified without changing their identity.

Common mutable types in Python:

- list
- dict
- set

Example:

```python
my_list = [1, 2, 3]
print(id(my_list))  # e.g., 140475642971136

my_list.append(4)
print(my_list)      # [1, 2, 3, 4]
print(id(my_list))  # Same ID – object was modified in place
```

## Immutable Objects

Immutable objects cannot be changed once they are created. Any operation that seems to modify them actually creates a new object.
Common immutable types in Python:

- int
- float
- str
- tuple

Example:

```python
s = "hello"
print(id(s))  # e.g., 140475642980512

s += " world"
print(s)      # "hello world"
print(id(s))  # Different ID – new object created
```

## Why It Matters
Understanding mutability is crucial because it affects how variables behave, especially when passed to functions. If you modify a mutable object, the change persists outside the function. If it's immutable, any change inside the function has no effect on the original object.

This behavior also helps prevent unexpected side effects in your code and improves debugging and memory management.

## How Arguments Are Passed to Functions
Python passes arguments by assignment. This means that functions receive a reference to the object, not a copy. However, the effect of that reference depends on whether the object is mutable or immutable.

Example with an immutable object (int):

```python
def increment(n):
    n += 1
    print("Inside function:", n)

x = 5
increment(x)
print("Outside function:", x)
# Output:
# Inside function: 6
# Outside function: 5
```

The value of x outside the function doesn't change.

Example with a mutable object (list):

```python
def add_item(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
add_item(my_list)
print("Outside function:", my_list)
# Output:
# Inside function: [1, 2, 3, 100]
# Outside function: [1, 2, 3, 100]
```

The list was modified inside the function, and the change is visible outside.

## Conclusion
The distinction between mutable and immutable objects is key to writing clean and predictable Python code. It influences how variables behave, how functions work, and how data is managed in memory. By understanding this, you'll avoid common bugs and write more efficient programs.
