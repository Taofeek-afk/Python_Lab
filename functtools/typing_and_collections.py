import copy
from collections.abc import MutableMapping

# collections.abc (Abstract Base Classes for Collections):

# Instead of inheriting from list or dict (which can lead to weird bugs because of built-in implementation details), you inherit from or implement protocols like collections.abc.Mapping, collections.abc.Sequence, or collections.abc.Container. This is how you build professional custom collections.
class SecureConfigStore(MutableMapping):
    """
    A secure configuration store that validates keys and values 
    and prevents internal state leakage via deep copies.
    """
    def __init__(self, initial_data=None):
        self._store = {}
        if initial_data:
            self.update(initial_data)

    def __getitem__(self, key: str):
        # SECURITY PRACTICE: Return a deep copy so callers 
        # cannot mutate internal nested dictionaries or lists in place.
        value = self._store[key]
        return copy.copy(value)

    def __setitem__(self, key: str, value):
        # SECURITY PRACTICE: Enforce validation rules on write
        if not isinstance(key, str):
            raise TypeError("Config keys must be strings to prevent injection/type juggling.")
        
        # Store a deep copy so external mutations don't pollute us
        self._store[key] = copy.copy(value)


    def __delitem__(self, key: str):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self) -> int:
        return len(self._store)

# --- Testing the Secure Container ---
config = SecureConfigStore({"db_host": "localhost", "permissions": ["read",]})

# Accessing returns a safe deep copy
perms = config["permissions"]
perms.append("root_admin") # Modifying local variable
# print(perms)

# print("Internal Store:", config["permissions"]) 
# Output: ['read'] -> Internal state is completely protected from outside tampering!


# Create Log Classes that have live span, create a class for each day, week, and month. You can subtract time to know how things occurred. 


from dataclasses import dataclass
from typing import Generic, List, TypeVar  # noqa: UP035

T = TypeVar("T")

@dataclass(frozen=True)
class AuditRecord:
    action: str
    user_id: int


@dataclass(frozen=True)
class NetworkPacket:
    payload: str


class SecureVault(Generic[T]):

    def __init__(self) -> None:
        self._storage: List[T] = []  # noqa: UP006

    def store(self, item: T) -> None:
        self._storage.append(item)

    def retrieve(self, index: int) -> T:
        return self._storage[index]


# --- Testing Type Safety ---
audit_vault = SecureVault[AuditRecord]()
audit_vault.store(AuditRecord(action="LOGIN", user_id=42))

print(audit_vault.retrieve(0))


from typing import Protocol


# 1. Define the Protocol (The structural contract)
class Auditable(Protocol):

  def get_audit_trail(self) -> str:
    ...  # Ellipsis means no implementation body required


# 2. Two completely unrelated classes
class DatabaseManager:
  # Notice: It does NOT inherit from Auditable!

  def get_audit_trail(self) -> str:
    return "DB query logs..."


class FirewallMonitor:
  # Unrelated class, also does not inherit from Auditable!

  def get_audit_trail(self) -> str:
    return "Packet drop logs..."


# 3. A function that accepts the Protocol type
def process_audit(target: Auditable):
  # Static type checkers know this is safe because 'target'
  # has a get_audit_trail() method returning a string!
  print(target.get_audit_trail())


# --- Execution ---
db = DatabaseManager()
firewall = FirewallMonitor()

process_audit(db)  # ✅ Valid! It has the required method.
process_audit(firewall)  # ✅ Valid! It also matches the structure.


# from typing import Protocol, runtime_checkable


# # 1. Add the @runtime_checkable decorator
# @runtime_checkable
# class Auditable(Protocol):

#   def get_audit_trail(self) -> str:
#     ...


# class DatabaseManager:

#   def get_audit_trail(self) -> str:
#     return "DB logs..."


# class BrokenManager:
#   # Missing get_audit_trail()
#   pass

# def process_audit(target):
#   # 2. Enforce it at runtime and raise an error!
#   if not isinstance(target, Auditable):
#     raise TypeError(
#         f"Object {type(target).__name__} does not satisfy the Auditable"
#         " protocol!"
#     )

#   print(target.get_audit_trail())


# # --- Execution ---
# db = DatabaseManager()
# process_audit(db)  # ✅ Passes smoothly

# broken = BrokenManager()
# process_audit(broken)  # 💥 Raises TypeError: Object BrokenManager does not satisfy the Auditable protocol!


from dataclasses import dataclass
from typing import ClassVar


@dataclass
class DatabaseConnection:
  # 🔴 ClassVar: Shared globally across ALL database connection instances
  supported_protocols: ClassVar[List[str]] = ["postgresql", "mysql"]  # noqa: UP006

  # 🟢 Instance Variable: Unique to each individual connection object
  host: str
  port: int


# Usage
conn1 = DatabaseConnection(host="localhost", port=5432)
conn2 = DatabaseConnection(host="remote.server", port=3306)

# Both instances share the exact same class-level list
print(conn1.supported_protocols)  # ['postgresql', 'mysql']
print(conn2.supported_protocols)  # ['postgresql', 'mysql']

# If you tried to pass supported_protocols into __init__, dataclass would ignore it
# because ClassVar explicitly excludes it from instance initialization.

