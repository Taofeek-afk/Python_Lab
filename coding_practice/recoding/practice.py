# # Metaprogramming: Dynamically creating a memory-optimized class
# DynamicUserClass = type(
#     "User", 
#     (object,), 
#     {
#         "__slots__": ["name", "email"],  # Memory optimization enforced!
#         "__init__": lambda self, name, email: (setattr(self, 'name', name), setattr(self, 'email', email))
#     }
# )

# u = DynamicUserClass("Alice", "alice@email.com")
# # u.age = 30  # Throws an AttributeError! Slots block unexpected mutations.
# print(help(type))



# 1. Define a function we want to use as a method
def roar_method(self):
    return f"{self.name} says ROAR!"

# 2. Dynamically build a "Lion" class out of thin air
Lion = type(
    "Lion",                  # Class Name
    (object,),               # Base/Parent classes
    {                        # Class body attributes/methods
        "species": "Panthera", 
        "__init__": lambda self, name: setattr(self, 'name', name),
        "roar": roar_method
    }
)

# 3. Instantiate and use it exactly like a normal class
simba = Lion("Simba") # type: ignore
# print(simba.species)  # type: ignore
# print(simba.roar())   # pyright: ignore[reportAttributeAccessIssue]


# A custom metaclass that intercepts class creation
class ForceUppercaseMeta(type):
    def __new__(cls, name, bases, dct):
        # Automatically make all attribute names uppercase
        uppercase_attr = {k.upper(): v for k, v in dct.items()}
        return super().__new__(cls, name, bases, uppercase_attr)

# Apply the metaclass
class SecretAgent(metaclass=ForceUppercaseMeta):
    codename = "007"
    weapon = "PPK"

agent = SecretAgent()
# print(agent.codename) -> Throws AttributeError!
# print(agent.CODENAME)  # type: ignore # Output: 007 (The metaclass changed it dynamically!)

zero = 0
one = 1
two = 2
three = 3

nums = [one, two, three,]
nums.insert(0, zero)
nums.reverse()
nums.sort()
nums.count(one)
# nums.clear()
# print(nums)

# def func(a = 1, b = 2):
#     return a+b


from functools import reduce, wraps

# from typing import Any

def reduce_sum(arr: list[int]) -> int:
    # from functools import reduce
    
    return reduce(lambda x, y: x + y, arr)


# print(reduce_sum([3, 4, 7, 1, 2]))


# Implement a function called process_orders that takes raw order data and returns the total revenue generated from valid, non-cancelled orders.
# Rules

#     zip: Combine the product names, unit prices, quantities, and order statuses into unified record tuples.

#     filter: Filter out any order where the status is 'cancelled'.

#     map: Calculate the total cost for each remaining item (price * quantity).

#     reduce: Sum all the individual item totals into a single


# from functools import partial


# def multiply(x: int, y: int) -> int:
#     return x * y


# # print(multiply(4, 3))

# double = partial(multiply, y=2)
# print(double(3))
# # It serves as a default Value!


# # Python 3.12+ Generic Function
# def get_first[T](items: list[T]) -> T | None:
#     print(type(T))
#     return items[0] if items else None

# # Preserves exact types:
# first_num = get_first([1, 2, 3])       # Type inferred as int | None
# first_str = get_first(["a", "b", "c"]) # Type inferred as str | None
# print(first_num)

memo = {}

def connection(**kwargs):
    if str(kwargs) in memo:
        print("Values returned from cache\n:")
        return memo[str(kwargs)]
    else:
        memo[str(kwargs)] = kwargs
    
    return kwargs


# print(connection(one=1, two=2, three=3, four=4))
# print()
# print(connection(one=1, two=2, three=3, four=4))


def my_decorator(func):
    @wraps(func)  # 1. Preserve original function metadata (__name__, __doc__)
    def wrapper(*args, **kwargs):  # 2. Accept any arguments passed to the target function
        # --- PRE-EXECUTION LOGIC ---
        
        result = func(*args, **kwargs)  # 3. Call original function and capture return value
        
        # --- POST-EXECUTION LOGIC ---
        
        return result  # 4. Return the result so caller receives it
    return wrapper  # 5. Return wrapper object to replace original function


def repeat(num_times):             # LEVEL 1: Accepts decorator arguments
    def decorator(func):           # LEVEL 2: Accepts the target function
        @wraps(func)
        def wrapper(*args, **kwargs): # LEVEL 3: Accepts function call arguments
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result # pyright: ignore[reportPossiblyUnboundVariable]
        return wrapper             # Level 1 returns Level 2
    return decorator               # Level 2 returns Level 3


@repeat(num_times=3)
def greet(name):
    return f"Hello, {name}"
    
# So @repeat(3) is simply a decorator factory—a function that creates and returns a decorator configured with your specific arguments!

import random


def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    attempts += 1
                    return func(*args, **kwargs)
                except Exception as e:  # noqa: BLE001
                    print(f"Attempt {attempts} failed with error: {e}. Retrying...")
            
            # If loop finishes without returning, all attempts failed
            raise RuntimeError(f"Function failed after {max_attempts} attempts.")
        return wrapper
    return decorator

@retry(max_attempts=3)
def rand():
    val = random.randint(5, 5)
    print(f"Generated: {val}")
    if val != 5:
        raise ValueError("Did not roll a 5!")
    return val


# print("Result:", rand())

# def flatten(nested):
#     if not nested:
#         return []
#     if isinstance(nested, list):
#         return flatten(nested[0]) + flatten(nested[1:])
#     print([nested])
#     return [nested]

# print(flatten([1, [3, 4, [4, 5], 6], 9]))


# outreachy
# gsoc
# google bla bla
#lfx mentorship
#year up united




class AgeDescriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called | instance: {instance} | owner: {owner}")
        return instance._age if instance else self

    def __set__(self, instance, value):
        print(f"__set__ called | instance: {instance} | value: {value}")
        if value < 0:
            raise ValueError("Age cannot be negative!")
        instance._age = value

class Person:
    age = AgeDescriptor()  # MUST be attached at the CLASS level!
    # print(age)

# p = Person()
# print(Person.age)
# p.age = 25   # Triggers: AgeDescriptor.__set__(p, 25)
# print(p.age) # Triggers: AgeDescriptor.__get__(p, Person)

# Write a descriptor class called BoundedNumber that enforces a minimum and maximum allowed numerical value.
# Requirements:

#     __init__(self, min_val, max_val): Accepts min_val and max_val.

#     __set_name__(self, owner, name): Automatically creates self.storage_name = f"_{name}".

#     __set__(self, instance, value):

#         If value < self.min_val or value > self.max_val, raise a ValueError.

#         Otherwise, save value inside instance.__dict__[self.storage_name].

#     __get__(self, instance, owner):

#         If instance is None (accessed via class, like Game.score), return self.

#         Otherwise, return the value stored in instance.__dict__.

#     __delete__(self, instance):

#         Deletes the attribute key from instance.__dict__.



# Here are some cool things you can do with descriptors:

# Lazy Evaluation / Computed Properties (@cached_property)
# You can calculate an expensive value the first time someone requests it, and then store it directly on the instance so it never has to be recalculated again.

# Type Checking & Enforcing Constraints
# You can ensure an attribute always stays within a certain range or data type (e.g., ensuring a percentage descriptor always rejects values below 0 or above 100).

# ORM Mappings (like Django or SQLAlchemy)
# In database frameworks, class attributes map directly to database columns. When you write user.email = "test@test.com", a descriptor intercepts that assignment to mark the row as "dirty" so the change automatically gets saved back to the SQL database.

# Attribute Aliasing or Deprecation
# If you change an attribute name in your code (e.g., changing user.fname to user.first_name), you can write a descriptor for fname that redirects requests to first_name and throws a warning log telling other developers to update their code.

