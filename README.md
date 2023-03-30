# Locksmith
### A simpler way to use locks in Python

--------------------

Typical lock usage in python looks like this:
```python
import threading
lock1 = threading.RLock()

def f1():
    lock1.acquire()
    try:
        pass  # do work here
    finally:
        lock1.release()
```

With Locksmith, you don't have to worry about instantiating, locking, and releasing locks. Just add a decorator to your functions.

```python
from locksmith import locked_function

@locked_function("lock1")
def f1():
    pass # do work here

```

Protecting Functions
-----------------

To protect a function from all concurrent access, use the decorator *locked_function* like in the example above.

Functions protected by this decorator can only be accessed by one thread at a time.

Protecting Object Methods
-------------------------
Since object methods may only interact with the attributes on that object, you can also use the *locked_method* decorator to protect object methods from concurrent access *on the same object*. That is to say, the method of an object can only be accessed by one thread at a time.

```python
from locksmith import locked_method

class MyClass:
    
    def __init__(self):
        self.protected = 0
        
    @locked_method("protected")
    def my_method(self):
        self.protected += 1

```
