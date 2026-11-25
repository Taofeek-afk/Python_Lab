# Objective: Write a descriptor that ensures an attribute can only be assigned values of a specific data type. If someone tries to assign the wrong type, raise a TypeError.

# Requirements:

# Create a descriptor class named Typed.

# It should accept an expected type (e.g., int, str, float) during its initialization (__init__).

# Implement __get__ and __set__ to store and retrieve the value safely using a private instance attribute (e.g., _value or similar).

# Create a class Product that uses Typed for a name (must be str) and a price (must be float or int).


class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
    
    def __set_name__(self, ObjType, var_name):
        self.var_name = var_name
    
    def __set__(self, obj, value):
        if type(value) != self.expected_type:
            raise TypeError(f"Expected an instance of {self.expected_type} got {type(value)}")
        obj.__dict__[self.var_name] = value
    
    def __get__(self, obj, ObjType):
        if obj is None:
            return f"Descriptor {self} of {type(self)} belongs to instances of {type(ObjType)}"
        return f"{self.var_name}: {obj.__dict__[self.var_name]}"


class Product:
    name = Typed(str)
    price = Typed(float)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# p = Product("Laptop", price=49.99)       
# print(p.name)
# print(p.price)



# Create a descriptor class named BoundedRange.

# It should accept a min_val and a max_val during initialization.

# In __set__, check if the incoming value falls inclusively between min_val and max_val. If it is too low or too high, raise a ValueError.

# Create a class Player with a level (range 1 to 100) and health (range 0 to 100) managed by this descriptor.

class BoundedRange:
    def __init__(self, min_val, max_val):
        self.min_val = min_val 
        self.max_val = max_val
    
    def __set_name__(self, ObjType, var_name):
        self.var_name = var_name
        
    def __set__(self, obj, value):
        # not self.max_val >= value >= self.min_val which is better, this? 
        if value > self.max_val or value < self.min_val: # or this?
            raise ValueError(f"Expected an input within {self.min_val} - {self.max_val}")
        obj.__dict__[self.var_name] = value
    
    def __get__(self, obj, ObjType):
        return obj if obj is None else obj.__dict__[self.var_name]
    

class Player:
    
    level = BoundedRange(1, 100)
    health = BoundedRange(0, 100)
    
    def __init__(self, level, health):
        self.level = level
        self.health = health


# player_1 = Player(1, 100)
# print(player_1.level)
# print(player_1.health)
# print(player_1.__dict__)


# Assignment 3: The Read-Only Token Descriptor
# Objective: Create a descriptor that allows an attribute to be set only once. Any subsequent attempts to modify it should raise an AttributeError or ValueError.

# Requirements:

# Create a descriptor class named ImmutableOnce.

# In __set__, check if the instance already has the private storage attribute (using hasattr() or checking __dict__).

# If it is already set, raise a ValueError("Cannot modify read-only attribute"). Otherwise, allow the assignment.

# Create a class UserSession with a read-only session_id.


class ImmutableOnce:
    def __set_name__(self, ObjType, var_name):
        self.var_name = var_name
        
    def __set__(self, obj, value):
        if self.var_name in obj.__dict__:
            raise ValueError("Cannot modify read-only attribute")
        obj.__dict__[self.var_name] = value
        
    def __get__(self, obj, ObjType):
        if obj is None:
            return self
        return obj.__dict__[self.var_name]


class UserSession:
    
    session_id = ImmutableOnce()
    
    def __init__(self, session_id):
        self.session_id = session_id


session = UserSession(234)

# print(session.session_id)
# print(session.__dict__)

# Objective: Build a custom version of Python's @cached_property using a non-data descriptor (a descriptor that implements __get__ but does not implement __set__).

# Requirements:

# Create a class CachedComputation.

# It should accept a function (the expensive method to compute) during __init__.

# When accessed via an instance for the first time, run the function, save the result directly into the instance's __dict__ under the function's name, and return the result.

# On subsequent accesses, because Python checks __dict__ before looking at class-level non-data descriptors, it will fetch the cached value instantly without running the function again!

import time


class CachedProperty:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        
        print(f"[{self.name}] Running expensive function for the first time...")
        time.sleep(2)
        
        value = self.func()
        
        obj.__dict__[self.name] = value
        
        return value


def expensive_task():
    return "42"


class Dataset:
    heavy_computation = CachedProperty(expensive_task)
    
    def __init__(self, title):
        self.title = title


def loading_spinner(duration_seconds=20):
    import sys
    import time
    
    spinner_frames = ['|', '/', '-', '\\']
    end_time = time.time() + duration_seconds
    i = 0

    print("Loading data... ", end="", flush=True)

    while time.time() < end_time:
        frame = spinner_frames[i % len(spinner_frames)]

        sys.stdout.write(f"\r\033[KLoading data... {frame}")
        sys.stdout.flush()
        
        time.sleep(0.1)  # Frame speed (10 FPS)
        i += 1

    sys.stdout.write("\r\033[KLoading data... Done!\n")
    sys.stdout.flush()

# loading_spinner(20)

