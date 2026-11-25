print()
print()

class A:
    def action(self):
        print("A action")

class B(A):
    def action(self):
        print("B action")

class C(A):
    def action(self):
        print("C action")

class D(B, C):
    pass

# P(D.__mro__)


class Root:
    def __init__(self):
        print("Root init")

class Left(Root):
    def __init__(self):
        print("Left init start")
        super().__init__()
        print("Left init end")

class Right(Root):
    def __init__(self):
        print("Right init start")
        super().__init__()
        print("Right init end")

class Diamond(Left, Right):
    def __init__(self):
        print("Diamond init start")
        super().__init__()
        print("Diamond init end")

# left = Left()
# right = Right()

# P()
# d = Diamond()
# P(Diamond.__mro__)
# P()


class SMSNotification:
    def send(self, recipient, message):
        return f"[SMS to {recipient}]: {message}"

class EmailNotification:
    def send(self, recipient, message):
        return f"[EMAIL to {recipient}]: {message}"


def dispatch_alert(notifier, recipient, message):
    print(f"Sending via {type(notifier)}...")
    return notifier.send(recipient, message)
    
sms_notifier = SMSNotification()
email_notifier = EmailNotification()

# print(dispatch_alert(email_notifier, "Taofeek", "Hello world!"))
# print(dispatch_alert(sms_notifier, "Taofeek", "Hello world!"))


class Engine:
    def start(self):
        return "Engine starting..."
    
class GPS:
    def navigate(self):
        return "Routing destination set"
    
class Vehicle:
    
    def __init__(self, engine, gps):
        self.engine = engine
        self.gps = gps
            
    def drive(self):
        self.engine.start()
        self.gps.navigate()


vehicle = Vehicle(engine=Engine(), gps=GPS())
vehicle.drive()

# class Vehicle(Engine, GPS):
    
#     def drive(self):
#         import time
        
#         self.start()
#         time.sleep(0.7)
#         self.navigate()

# vehicle = Vehicle()
# vehicle.drive()

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def __repr__(self):
        return f"Server(host={self.host!r}, port={self.port})"

    def __str__(self):
        return f"Active Server at {self.host!r}:{self.port}"

# srv = Server("127.0.0.1", 8080)
# print(repr(srv))  # Server(host='127.0.0.1', port=8080)
# print(srv)        # Active Server at 127.0.0.1:8080 (Falls back to __str__)


class PriorityTask:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
        
    def __eq__(self, other):
        if not isinstance(other, PriorityTask):
            return NotImplemented
        
        return self.priority == other.priority # This is returning false, I expected True for 
    
    def __lt__(self, other):
        if not isinstance(other, PriorityTask):
            return NotImplemented
        
        return self.priority > other.priority
    
    def __le__(self, other):
        if not isinstance(other, PriorityTask):
            return NotImplemented
        
        return self.priority >= other.priority

        
# print(dir(PriorityTask)) # eq, ge, gt, le, lt,

from functools import total_ordering


@total_ordering
class Product:
    
    def __init__(self, name: str, price: float, rating: int):
        self.name = name
        self.price = price
        self.rating = rating
    
    def __eq__(instance_1, instance_2): # type: ignore
        if not isinstance((instance_1, instance_2), Product):
            return NotImplemented
        
        return (instance_1.name == instance_2.name) and (instance_1.price == instance_2.price)
    
    def __lt__(instance_1, instance_2): # type: ignore
        if not isinstance((instance_1, instance_2), Product):
            return NotImplemented
        
        return instance_1.price < instance_2.price


from typing import Any


class CustomPlaylist:
    
    def __init__(self, items = None):
        self._items = list(items) if items else [] # type: ignore
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return f"CustomPleylist({self._items[index]})"
    
    def __setitem__(self, index, values: Any):
        self._items[index] = values
    
    def __iter__(self):
        for song in self._items:
            print(f"Now playing [{song}]")
            yield song
    
    def __repr__(self):
        return f"CustomPlaylist(items={self._items!r})" # Is the !r useless in the f string since it's a list??

from abc import ABC, abstractmethod


class DataStore(ABC):
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def write(self, data: str):
        pass
    
    def disconnect(self):
        print("Disconnecting from storage...")

# try:
#     datastore = DataStore()
# except TypeError:
#     print("Can't instantiate abstract class")

class PostgresStore(DataStore):
    
    def write(self): # type: ignore
        ...
    
    def disconnect(self):
        ...
    
    def connect(self):
        ...
    

db = PostgresStore()
# print(db.connect())


class SlottedUser:
    __slots__ = ("email", "name")
    
    def __init__(self, email, name):
        self.email = email
        self.name = name
    
user_1 = SlottedUser("@gmail.com", "Taofeek")

class ManagedTransaction:
    def __init__(self, transaction_name):
        self.transaction_name = transaction_name

    def __enter__(self):
        print(f"[START]: Opening transaction '{self.transaction_name}'...")
        return self  # Bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"[ERROR]: Exception detected: {exc_val}. Rolling back transaction!")
            return False  # Let the exception propagate outward
        else:
            print(f"[COMMIT]: Transaction '{self.transaction_name}' successful.")
            return True
        
    def trans_name(self):
        return self.transaction_name


# --- Testing Exception Handling ---
# try:
#     with ManagedTransaction("Faulty_Transfer") as tx:
#         print("Executing operations...")
#         raise ValueError("Insufficient funds!")
# except ValueError:
#     print("Caught propagated exception outside the context block.")

import time


class Timer:
    def __enter__(self):
        # Record the start timestamp
        self.start_time = time.perf_counter()
        print("Timer started...")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is not None:
            print("Timer aborted due to an exception.")
            return False  # Let the exception propagate
        
        # Record the end timestamp and compute the delta
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time
        print(f"Timer stopped. Elapsed: {elapsed:.4f} seconds")
        return True


# with Timer():
#     print("Executing block of work...")
#     time.sleep(1.2)

# Connection pooling
class Connection:
    def __init__(self, conn_id):
        self.conn_id = conn_id

class ConnectionPool:
    def __init__(self, size=3):
        # Pre-create a pool of 3 database connections
        self._pool = [Connection(i) for i in range(size)]

    def acquire(self):
        if not self._pool:
            raise Exception("Pool exhausted! No connections available.")  # noqa: TRY002
        return self._pool.pop()  # Take one out

    def release(self, conn):
        self._pool.append(conn)  # Return it back for reuse

# Testing the pool
# pool = ConnectionPool(size=2)
# conn1 = pool.acquire()
# print(f"Acquired connection: {conn1.conn_id}")

# pool.release(conn1) # Returned safely to pool

class SingletonDatabase:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Allocate memory only once
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, connection_url="localhost:5432"):
        # Prevent re-initialization if the singleton already exists
        if not getattr(self, "_initialized", False):
            self.connection_url = connection_url
            self._initialized = True


db1 = SingletonDatabase("postgres://primary")
db2 = SingletonDatabase("postgres://secondary")

print(db1.__dict__)
print(db2.__dict__)
