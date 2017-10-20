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
