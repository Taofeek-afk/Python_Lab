class Strict(type):
    def __new__(mcs, name, bases, namespace):
        # 'mcs' is the metaclass itself
        # 'name' is the name of the class being created (e.g. "UserService")
        # 'bases' is a tuple of parent classes
        # 'namespace' is a dictionary of all methods/attributes defined inside the class body
        
        if "version" not in namespace:
            namespace["version"] = "1.0"
        
        return super().__new__(mcs, name, bases, namespace) 


class UserService(metaclass=Strict):
    pass


service_1 = UserService()

# print(service_1.__dict__)
# print(service_1.version) # type: ignore


# Write a custom metaclass named ValidateAttributesMeta:

# Create a metaclass inheriting from type.

# Inside __new__, check the namespace dictionary to ensure that any class using this metaclass defines a method named execute.

# If execute is missing from the class definition, raise a TypeError immediately when the class is parsed.

# Create a valid test class that implements execute and prove it compiles, then create an invalid class missing execute to prove it catches the error at class definition time.

class ValidatedAttributesMeta(type):
    def __new__(metaclass, instantiated_obj, parent_classes, namespace): # type: ignore
        if "execute" not in namespace or not callable(namespace["execute"]):
            raise TypeError("Class must implement the execute method")
        
        return super().__new__(metaclass, instantiated_obj, parent_classes, namespace)


class abstract_class_1(metaclass=ValidatedAttributesMeta):
    def execute(self):
        ...
    
    def __repr__(self):
        return "abstract_class_1(*args=None, **kwargs=None)"

test_case_1 = abstract_class_1()
# print(test_case_1)


class abstract_class_2(metaclass=ValidatedAttributesMeta):   
    def __repr__(self):
        return "abstract_class_1(*args=None, **kwargs=None)"


test_case_2 = abstract_class_2()
# print(test_case_2)


class PluginRegistryMeta(type):
    registry = {}  # Global dictionary to track all registered plugins  # noqa: RUF012

    def __new__(mcs, name, bases, namespace):
        # Create the class normally first
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Skip registering the base interface itself, only register actual plugins
        if name != "BasePlugin":
            plugin_name = namespace.get("plugin_name", name.lower())
            print(f"[Registry]: Automatically registering plugin -> '{plugin_name}' ({name})")
            PluginRegistryMeta.registry[plugin_name] = cls
            
        return cls


class BasePlugin(metaclass=PluginRegistryMeta):
    def parse(self, data):
        raise NotImplementedError


class JSONParserPlugin(BasePlugin):
    plugin_name = "json"
    def parse(self, data):
        return f"Parsing JSON data: {data}"


class XMLParserPlugin(BasePlugin):
    plugin_name = "xml"
    def parse(self, data):
        return f"Parsing XML data: {data}"


print("\nActive Registry Contents:", PluginRegistryMeta.registry)

chosen_format = "json"
parser_class = PluginRegistryMeta.registry[chosen_format]
active_parser = parser_class()

print(active_parser.parse("{'user': 'Taofeek'}"))


# a central file (often called a registry hub, main.py, or router.py) is a single file where you would normally have to manually import every single module, class, and extension your application uses.

# # Add methods dynamically
# def greet(self): return "hi"
# MyClass.greet = greet

# # Modify class at definition time
# def make_class(name, attrs):
#     return type(name, (), attrs)

# a package containing an __init__.py file) is a directory
