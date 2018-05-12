# Make Object jsonable

python's built-in json lib support custom object serialization
by passing a JSONDecoder and JSONEncoder, whose default() method
must be overridden.

However, if json moudule is hidden behind a framework, it's
impossible to pass the encoder/decoder to json module. Here
summarize some solutions:

1. inherit list and override its iterator
2. inherit dict and override items() and iteritems()
3. make a monkey patch to the json module


**Warning**

It's easy to encounter "multiple bases have instance lay-out conflict"
if inheriting built-in class such as list and dict as well as using _\_slots_\_

This error is caused by the C layout conflit and it seems there is no easy way
to solve it.

warp the class?


# Unittest

test case dependency and order


# Skill


## Avoid __getattribute__ recursion

__getattribute__ is the entry of all access request to class and obj

object.__getattribute__(obj, '<your member name>')
type(obj).__getattribute__(obj, '<your member name>')


# Python3 Example


## Enum


```
from enum import Enum


class Rectangle(Enum):
    SMALL = (5, 1)
    MEDIUM = (10, 2)
    LARGE = (15, 3)

    def __init__(self, length, width):
        # If __new__() or __init__() is defined the value of
        # the enum member will be passed to those methods without calling super
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width


small = Rectangle.SMALL
print(small.square())
print(small.name, small.value)
print(small.length, small.width)

for name, instance in Rectangle.__members__.items():
    print(name, instance)

---

5
SMALL (5, 1)
5 1
SMALL Rectangle.SMALL
MEDIUM Rectangle.MEDIUM
LARGE Rectangle.LARGE
```

