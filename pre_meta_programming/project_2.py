# Project 2: The Fault-Tolerant Object Pool & Transaction Context Manager
# Core Concepts Tested: Object Pooling, Context Managers (__enter__/__exit__), and Exception Suppression/Propagation.

# The Goal: Build a resource management system that pools expensive worker objects, allows users to check them out safely using a with statement, and automatically handles rollback and recycling if a failure occurs.

# Requirements:
# Create a Worker class that has a unique ID and a status (e.g., "IDLE", "BUSY", "DEAD").

# Create an ObjectPool class that pre-allocates a fixed number of Worker instances (e.g., a pool of 3). It must have .acquire() and .release() methods.

# Build a custom context manager class named PooledTransaction. When entered, it grabs an available worker from the pool. If work succeeds, it releases the worker back to the pool cleanly. If an exception crashes the with block, it marks the worker as "DEAD", discards it, creates a fresh replacement worker for the pool, and cleanly propagates the exception outward.

class Worker:
    def __init__(self, id, status="IDLE"):
        self.id = id
        self.status = status

    def __repr__(self):
        return f"Worker(id={self.id}, status='{self.status}')"


class ObjectPool:
    def __init__(self, size=3):
        self.workers = [Worker(i, "IDLE") for i in range(1, size + 1)]
        self._next_id = size + 1

    def acquire(self):
        for worker in self.workers:
            if worker.status == "IDLE":
                worker.status = "BUSY"
                return worker
        raise RuntimeError("No available workers in the pool.")

    def release(self, worker):
        if worker not in self.workers:
            raise ValueError("This worker does not belong to this pool.")
        if worker.status != "BUSY":
            raise ValueError("You cannot release a worker that is not currently busy.")
        worker.status = "IDLE"

    def discard_and_replace(self, worker):
        if worker in self.workers:
            self.workers.remove(worker)
        
        worker.status = "DEAD"
        
        fresh_worker = Worker(self._next_id, "IDLE")
        self._next_id += 1
        self.workers.append(fresh_worker)


class PooledTransaction:
    def __init__(self, pool):
        self.pool = pool
        self.worker = None

    def __enter__(self):
        self.worker = self.pool.acquire()
        return self.worker

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.pool.discard_and_replace(self.worker)
            return False
        self.pool.release(self.worker)
        return True

pool = ObjectPool(size=3)
print("Initial Pool:", pool.workers)


with PooledTransaction(pool) as worker:
    print(f"Acquired: {worker}")


print("Pool after success:", pool.workers)

try:
    with PooledTransaction(pool) as worker:
        print(f"Acquired for failing job: {worker}")
        raise ValueError("Something went wrong during work!")
except ValueError as e:
    print(f"Caught expected exception: {e}")

print("Pool after failure (Notice the new replacement worker ID 4):", pool.workers)

# def profile(name, /, *, age):
#     print(name, age)

# profile("Ayo", age=17)
