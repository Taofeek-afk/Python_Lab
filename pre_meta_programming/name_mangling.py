P = print

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._pin = 1234            # Protected (convention)
        self.__balance = balance         # Private -> triggers Name Mangling!

    def get_balance(self):
        # Inside the class, __balance is automatically translated to _BankAccount__balance
        return self.__balance # type: ignore


# account = BankAccount("Alice", 5000.0)
# print(account.get_balance())
# print(account._BankAccount__balance) # type: ignore
# print(BankAccount.get_balance(account))


class Parent:
    def __init__(self):
        self.__secret = "Parent Secret"

    def reveal_parent(self):
        return self.__secret  # Mangles to _Parent__secret


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child Secret"  # Mangles to _Child__secret

    def reveal_child(self):
        return self.__secret  # Mangles to _Child__secret


# c = Child()
# print(c.reveal_parent())  # Output: "Parent Secret"
# print(c.reveal_child())   # Output: "Child Secret"

# print(c.__dict__)
# Notice how BOTH secrets coexist safely without overwriting each other:
# {
#    '_Parent__secret': 'Parent Secret', 
#    '_Child__secret': 'Child Secret'
# }

class Father:
    def __init__(self):
        self.father_name = "Zhou Ling"
    
    def get_name(instance): # type: ignore
        return instance.father_name


class Son(Father):
    def __init__(instance): # type: ignore
        super().__init__()
        instance.father_name = "Li Hao"
    
    def get_name_2(instance): # type: ignore
        return instance.father_name


s = Son()

# print(s.get_name())
# print(s.get_name_2())


# Rigorous Classwork: Module 1.1
# Write a Python class named SecureVault that incorporates the following architectural rules:

# It must accept a string vault_id and a float security_level in its initializer.

# Store vault_id as a public attribute.

# Store security_level as a protected attribute (_security_level).

# Store a sensitive string encryption_key as a private attribute (__encryption_key), relying on name mangling.

# Implement a method called verify_key(self, candidate_key) that returns True if the candidate matches the mangled encryption key, and False otherwise, without exposing the key externally.

# Write test assertions or print statements proving that trying to access vault.__encryption_key throws an AttributeError, but accessing it via vault._SecureVault__encryption_key succeeds.

class SecureVault:
    def __init__(self, vault_id: str, security_level: float):
        self.vault_id = vault_id
        self._security_level = security_level
        self.___encryption_key = "Hash256"
    
    def verify_key(self, candidate_key):
        return self.___encryption_key == candidate_key
    
    def get_key(self):
        # Created for assertion purpose
        return self.___encryption_key + " "
    

vault = SecureVault("1", 3.)
# print(vault._security_level)
# print(vault.__dict__)

P(vault.verify_key("Hash256"))

try:
    P(vault.___encryption_key)
except AttributeError:
    print(...)

P(vault._SecureVault___encryption_key) # type: ignore

