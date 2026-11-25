class CustomProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        if instance is None:
            return self 
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)  # Call the getter function, passing the instance as 'self'

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)  # Call the setter function

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)



class Person:
    def __init__(self, name):
        self._name = name

    def name(self): # type: ignore
        return self._name.upper()
    
    def name_setter(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value * 2
    
    name = CustomProperty(fget=name, fset=name_setter, fdel=None)
    
        
p = Person("Alice")
print(p.name)       # Triggers CustomProperty.__get__ -> "Alice"
p.name = "Bob"      # Triggers CustomProperty.__set__
print(p.name)       # "Bob"


# class CustomStaticMethod:
#     def __init__(self, func):
#         self.func = func

#     def __get__(self, instance, owner):
#         # Returns the raw function directly whether accessed via instance or class
#         return self.func


# # --- Testing CustomStaticMethod ---
# class MathUtils:
#     @CustomStaticMethod
#     def add(a, b):
#         return a + b

# print(MathUtils.add(2, 3))  # 5
# print(MathUtils().add(2, 3)) # 5 (No 'self' or 'cls' injected)




# import types


# class CustomClassMethod:
#     def __init__(self, func):
#         self.func = func

#     def __get__(self, instance, owner):
#         # Bind the function to the 'owner' (the class) instead of the 'instance'
#         return types.MethodType(self.func, owner)


# # --- Testing CustomClassMethod ---
# class Config:
#     DEFAULT_ENV = "production"

#     @CustomClassMethod
#     def get_env(cls):
#         return cls.DEFAULT_ENV

# print(Config.get_env())  # "production" (Config class passed automatically as cls)
