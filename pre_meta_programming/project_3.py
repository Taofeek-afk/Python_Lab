# Project 3: The Auto-Registering Plugin CLI Router
# Core Concepts Tested: ABCs, Plugin Metaclass Registries, Container Protocols (__getitem__, __len__, __iter__), and Duck Typing.

# The Goal: Build a command-line interface (CLI) plugin router where adding a new command file automatically registers it into a global registry, and the router acts as an iterable container.

# Requirements:
# Create an Abstract Base Class named BaseCommand with an abstract method execute(self, args). Done

# Create a metaclass named CommandRegistryMeta that automatically registers any subclass of BaseCommand into a centralized dictionary based on a class-level attribute command_name.

# Create a CommandRouter class that implements the container and sequence protocols (__len__, __getitem__, __iter__) using the registered metaclass data. This allows you to loop through all available commands using a standard for loop or check if a command exists using in.

from abc import ABC, ABCMeta, abstractmethod


class CommandRegistryMeta(ABCMeta): # used ABCMeta because type was throwing an error, can't inherit from differet metaclasses. 
    registry = {}  # noqa: RUF012
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace) # type: ignore
        
        if "command_name" in namespace and namespace["command_name"] is not None: # namespace.get("command_name", False) is this a better alternative?
            cmd_name = namespace["command_name"]
            mcs.registry[cmd_name] = cls
        
        return cls


class BaseCommand(ABC, metaclass=CommandRegistryMeta):
    
    @abstractmethod
    def execute(self, *args):
        pass

class CommandRouter(BaseCommand): # type: ignore
    def execute(self, *args): # type: ignore
        return ...

    def __len__(self):
        return len(CommandRegistryMeta.registry)
    
    def __getitem__(self, key):
        return CommandRegistryMeta.registry[key]
    
    def __iter__(self):
        return iter(CommandRegistryMeta.registry)
    

commands = CommandRouter()
print(commands.__dict__)
print(len(commands))


# print(commands) # TypeError: super.__new__(CommandRegistryMeta): CommandRegistryMeta is not a subtype of super
    # def __new__(cls: type[Self], name: str, bases: tuple[type, ...], namespace: dict[str, Any], /, **kwds: Any) -> Self:
    #     return super().__new__(name, bases, namespace, **kwds)


# what special symbols can be written __ _____ the likes of * / ** and @ and how are they used?


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # This intercepts class instantiation!
        print("They called me.")
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print("I pass once")
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    pass

# Every time you call Database(), it returns the exact same instance!
db1 = Database()
db2 = Database()
# print(SingletonMeta.__dict__)
print(db1 is db2)  # True (Singleton pattern implemented via metaclass dunder!)

