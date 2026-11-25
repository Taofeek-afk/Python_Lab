# Project 1: The "ORM-Lite" Field Validator & Schema Registry
# Core Concepts Tested: Descriptors, Metaclasses, __slots__, and Class Inspection.

# The Goal: Build a mini Object-Relational Mapper (ORM) system where classes define their fields using descriptor classes, and a metaclass automatically registers the schema and validates inputs at runtime.

# Requirements:
# Create a data descriptor class named Field (or specific subclasses like IntegerParam and StringParam) that handles type checking and attribute storage. If someone passes the wrong type, raise a TypeError. # Done

# Create a custom metaclass named ModelMeta. When any model class is defined using this metaclass, it should inspect the class namespace, pull out all the Field descriptors, and store them in a class-level dictionary called _schema. Done

# Create a base class Model using ModelMeta. When you instantiate a model (e.g., user = User(age=25, name="Alice")), it should use the schema to validate the incoming keyword arguments against the descriptors before saving them. 

class IntegerParam:
    
    def __set_name__(self, ObjType, var_name): # type: ignore
        self.var_name = var_name
    
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"Expected an instance of an int, got a {type(value)}")
        obj.__dict__[self.var_name] = value
    
    def __get__(self, obj, ObjType):
        if obj is None:
            return self
        return obj.__dict__.get(self.var_name)


class StrParam:
    
    def __set_name__(self, ObjType, var_name):
        self.var_name = var_name
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected an instance of str, {type(value)} passed")
        obj.__dict__[self.var_name] = value
    
    def __get__(self, obj, ObjType):
        if obj is None:
            return self
        return obj.__dict__.get(self.var_name)


class ModelMeta(type):
       
    def __new__(mcs, name, base, namespace):
        # print(type(name), name)
        # print(type(mcs), mcs)
        # print(type(namespace), namespace)
        # print(type(base), base)
        
        # name.schema_dict = {} # If this is served as a str, how do I assign value to user?
        schema_dict = {}

        for value in namespace:
            if hasattr(namespace[value], "__set__"):
                schema_dict[value] = namespace[value]
        
        # print(schema_dict)
              
        cls = super().__new__(mcs, name, base, namespace)
        cls.schema_dict = schema_dict # type: ignore
        
        return cls


class User(metaclass=ModelMeta):
    
    name = StrParam()
    age = IntegerParam()
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.schema_dict: # type: ignore
                raise AttributeError(f"{type(self)} does not expect a value named {key}")
            setattr(self, key, value) 
            
        missing = set(self.schema_dict).difference(set(self.__dict__)) # type: ignore

        if missing:
            raise KeyError(f"Expected {len(missing)} more values: {[x for x in missing]}")


model_1 = User(name="Ayo", age=17)  
