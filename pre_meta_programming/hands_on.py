# ### Tier 1: OOP Basics (Encapsulation & State Integrity)

# *Focus: Class definition, instance attributes, private state (`_` / `__`), validation, and basic instance methods.*
# Problem Statement: The Robust Bank Account System

# Build a Python class named `BankAccount` that models a secure financial account.
# 1. **Initialization:** It should accept an `account_holder` (string) and an optional `initial_balance` (default to `0.0`). The balance cannot be negative upon creation (raise a `ValueError` if it is).
# 2. **Encapsulation:** The actual balance attribute must be kept private (e.g., `_balance` or `__balance`) so external code cannot manually hack or overwrite it.
# 3. **Methods:**
# * `deposit(amount)`: Adds money. Must validate that the amount is strictly greater than zero.
# * `withdraw(amount)`: Subtracts money. Must validate that there are sufficient funds and the amount is positive; otherwise, raise a `ValueError`.
# * `get_balance()`: A getter method to safely view the balance.
# 4. **Audit Trail:** Maintain an internal transaction log list (e.g., `["Deposited 100", "Withdrew 50"]`) that records every successful transaction.
class InsufficientFunds(ValueError):
    pass


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        BankAccount.validator(initial_balance)
        self.account_holder = account_holder
        self._initial_balance: int = initial_balance
        self._audit_trail = []
        
    @staticmethod
    def validator(value, min=0):
        if value < min:
            raise ValueError("Balance should be a non-negative value")
    
    @property
    def initial_balance(self):
        return self._initial_balance
    
    @initial_balance.setter
    def initial_balance(self, value):
        BankAccount.validator(value)
        self._initial_balance = value
    
    def deposit(self, value):
        BankAccount.validator(value, 1)
        self._initial_balance += value
        self._audit_trail.append(f"Deposited {value}")
    
    def withdraw(self, value):
        BankAccount.validator(self._initial_balance, value)
        if value > self._initial_balance:
            raise InsufficientFunds("Insufficient funds for this withdrawal")
        self._initial_balance -= value
        self._audit_trail.append(f"Withdrew {value}")
    
    def get_balance(self):
        return self._initial_balance
    
    def view_audit(self):
        for log in self._audit_trail:
            print(log)
  

# acct_1 = BankAccount("Taofeek", 87)
# print(acct_1.get_balance())
# acct_2 = BankAccount.__new__(BankAccount)
# BankAccount.__init__(acct_2, "Taiwo")
# BankAccount.deposit(acct_2, 65)
# print(BankAccount.get_balance(acct_2))
# print(BankAccount.validator(67)) # Can the vaidator method be used on instances of other classes?

# Tier 2: OOP Intermediate (Polymorphism, Inheritance & Composition)

# *Focus: Abstract Base Classes, method overriding, super() calls, composition, and dunder protocols like `__str__` and `__eq__`.*

# Problem Statement: The Polymorphic Media Library

# Design a media catalog system using inheritance and composition.

# 1. **Abstract Base Class (`MediaItem`):**
# * Must inherit from `abc.ABC`.
# * Requires attributes: `title` (str), `duration_minutes` (int).
# * Must have an abstract method: `get_media_type(self) -> str`.
# * Must implement a concrete `__str__` method returning a clean summary string.

# 2. **Concrete Subclasses:**
# * Create `Movie` (adds `director` attribute, `get_media_type` returns `"Movie"`).
# * Create `Podcast` (adds `host` attribute and `episode_number` int, `get_media_type` returns `"Podcast"`).

# 3. **The Composition Container (`MediaLibrary`):**
# * Create a container class `MediaLibrary` that holds a collection of `MediaItem` objects internally.
# * Implement container protocols: `__len__`, `__iter__`, and `__getitem__` so you can loop through the library and index items directly.
# * Add a search method: `find_by_title(title)` that returns matching items.

from abc import ABC, abstractmethod


class MediaItem(ABC):
    
    @abstractmethod
    def __init__(self, title: str, duration_minutes: int) -> None:
        self.title = title
        self.duration_minutes = duration_minutes
    
    @abstractmethod
    def get_media_type(self) -> str:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        return f"[{self.get_media_type()}] '{self.title}' ({self.duration_minutes} mins)"

class Movie(MediaItem):
    def __init__(self, title, duration_minutes, director):
        super().__init__(title, duration_minutes)
        self.director = director
    
    def get_media_type(self) -> str:
        return type(self).__name__
    
    def __str__(self) -> str:
        return super().__str__()

class Podcast(MediaItem):
    def __init__(self, host, episode_number, title, duration_minutes):
        super().__init__(title, duration_minutes)
        self.host = host
        self.episode_number = episode_number
    
    def get_media_type(self) -> str:
        return type(self).__name__
    
    def __str__(self):
        return super().__str__()

class MediaLibrary:
    def __init__ (self, *args):
        self._items = [arg for arg in args if isinstance(arg, MediaItem)]
    
    def __len__ (self):
        return len (self._items)
    
    def __iter__ (self):
        return iter (self._items)
    
    def __getitem__(self, key):
        return self._items[key]
    
    def find_by_title (self, title):
        return [(media.title, media) for media in self._items if media.title.lower() == title.lower()]


movie_1 = Movie("Introduction to programming fundamentals", 45, "David")
podcast_1 = Podcast("Spotify", 23, "Hello world!", 34)

library = MediaLibrary(movie_1, podcast_1, "audio", "text")

# for match in library:
#     print(f"Found: {match.title} directed by ...")

# print(library.find_by_title("Introduction to programming fundamentals"))


# ### Tier 3: OOP Advanced (Descriptors, Custom Protocols & Lifecycle Control)

# *Focus: Descriptors, memory optimization, context managers, and custom control flow.*

# Problem Statement: The Transaction-Safe Inventory & Weight Guard

# Build an advanced inventory management system for a game engine that enforces strict physical constraints and transaction safety.

# 1. **Descriptor Validation (`BoundedInt`):**
# * Build a custom data descriptor class `BoundedInt` that ensures an item's quantity or weight can never drop below zero or exceed a maximum cap set during descriptor initialization. If violated, raise a `ValueError`.

# 2. **Slotted Item Class (`Item`):**
# * Create an `Item` class using `__slots__` to optimize memory, holding `name`, `weight` (using your `BoundedInt` descriptor), and `quantity`.

# 3. Context Manager Rollback (`InventoryTransaction`):
# * Build a custom context manager class named `InventoryTransaction` that accepts an inventory manager object.
# * If an operation inside the `with` block crashes (e.g., inventory becomes overweight or runs out of stock), the context manager's `__exit__` must automatically **rollback all inventory changes** made during that block and safely suppress or propagate the exception.

# webpages audio narration.
import copy


class BoundedInt:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        
    def __set_name__(self, ObjType, var_name):
        self.private_name = f"_{var_name}"
    
    def __set__(self, instance, value):
        if not isinstance(value, int) or not (self.max_val >= value >= self.min_val):
            raise ValueError(f"Value must be between {self.min_val} and {self.max_val}")
        setattr(instance, self.private_name, value)# Error, instance.private_name = value It does npot evaluate private_name
    
    def __get__(self, instance, _): # _ = Owner or objectType
        if instance is None:
            return self
        return getattr(instance, self.private_name) # why doesn't instance.self.private_name work here?? 

class Item:
    
    quantity = BoundedInt(1, 100)
    weight = BoundedInt(1, 100)
    
    __slots__ = ("_quantity", "_weight", "name")
    
    def __init__(self, name, quantity, weight):
        self.name = name
        self.quantity = quantity
        self.weight = weight

class Inventory:
    def __init__ (self, *args: Item, size=4) -> None:
        self.items = []
        self.size = 4
        
        for arg in args:
            self.add_item(arg)
    
    def check_item(self, item: Item): # get back to
        if not isinstance(item, Item):
            raise TypeError("Expected an instance of Item")
        return item in self.items

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise TypeError("Expected an instance of Item")
        if item in self.items:
            raise ValueError("Item already exists in the inventory")
        if len(self.items) == self.size:
            raise RuntimeError("No more space in inventory to add items")
        self.items.append(item)
    
    def remove_item(self, item: Item):
        if item not in self.items:
            raise ValueError("Item is not part of this inventory")
        self.items.remove(item)
        
    def increase_size(self, size):
        if size < 1:
            raise ValueError("Expected a value greater than 0")
        self.size += size
        
    def __len__(self):
        return len(self.items)

class InventoryTransaction:
    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory
        self._backup_items = None
        self._backup_size = None
            
    def __enter__(self):
        self._backup_items = copy.deepcopy(self.inventory.items)
        self._backup_size =  self.inventory.size

        return self.inventory
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
           self.inventory.items = self._backup_items # type: ignore
           self.inventory.size = self._backup_size

           return False
    
        return True

# with InventoryTransaction() as item_inventory:
#     item = item_inventory[0]
    
    
#     item_1 = item("food", 24, 12)
#     item_2 = item("Fruit", 10, 6) 
#     item_3 = item("Sword", 50, 10.5)
#     item_4 = item("Water", 20, 5.5)
#     item_5 = item("Shield", 20, 72.5)
    
#     inventory = item_inventory[1](item_1, item_2, item_3)
#     print(len(inventory))
#     inventory.add_item(item_4)
#     print(len(inventory))
#     inventory.size += 2
#     inventory.add_item(item_5)
#     print(len(inventory))
#     print(inventory.check_item(item_3))
        
   
# import time
# import traceback
# My weaknesses are context_managers, metaclasses and iter. I would like to learn flags like chmod 777 and others/ 
# class ErrorLoggingMeta(type):
#     def __new__(mcs, name, bases, namespace):
#         # Loop through all items in the class namespace
#         for key, value in namespace.items():
#             # If it's a function (method), wrap it with a try/except logger
#             if callable(value):
#                 namespace[key] = mcs._wrap_method(value)
                
#         return super().__new__(mcs, name, bases, namespace)

#     @staticmethod
#     def _wrap_method(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 # Capture the full traceback as a string
#                 tb_str = traceback.format_exc()
                
#                 # Report/log to a file
#                 with open("error_log.txt", "a") as f:
#                     f.write(f"[{time.ctime()}]] Error in {func.__name__}: {e}\n")
#                     f.write(tb_str + "\n" + "-"*40 + "\n")
                
#                 # Re-raise the exception so the program still knows it crashed
#                 raise
#         return wrapper


# class Calculator(metaclass=ErrorLoggingMeta):
#     def divide(self, a, b):
#         return a / b


# --- Testing it ---
# calc = Calculator()
# try:
#     calc.divide(10, 0)
# except ZeroDivisionError:
#     print("Caught the division error! Check 'error_log.txt'.")

# Syntax: type(name_of_class, tuple_of_base_classes, dictionary_of_attributes)

# Dynamically creating a class named 'Dog' with a bark method:
Dog = type(
    "Dog",                          # Class name
    (),                             # Base classes (inheritance) # type: ignore
    {
        "species": "Canine",
        "bark": lambda self: "Woof!"
    }
)

# --- Using the dynamic class ---
# my_dog = Dog()
# print(my_dog.species)  # Canine
# print(my_dog.bark())   # Woof!
# print(type(my_dog))    # <class '__main__.Dog'>


