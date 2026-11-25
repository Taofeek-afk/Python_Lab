import threading
import time


def worker_task(name, delay):
    print(f"Thread {name}: starting")
    time.sleep(delay)  # Simulating I/O or work
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    print("Main program: starting threads")
    
    # Create two threads
    t1 = threading.Thread(target=worker_task, args=("Alpha", 2))
    t2 = threading.Thread(target=worker_task, args=("Beta", 1))
    
    # Start them running concurrently
    t1.start()
    t2.start()
    
    # Wait for both to finish
    t1.join()
    t2.join()
    
    print("Main program: all threads done")

counter = 0

def increment():
    global counter
    for _ in range(100_000):
        # This looks like one line, but in bytecode, 
        # it is read -> add 1 -> write back!
        counter += 1


if __name__ == "__main__":
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"Final counter value: {counter}")
    print("Expected value: 100,000")


print(counter)


# counter = 0
# # Create a lock object
# lock = threading.Lock()

# def safe_increment()
#     global counter
#     for _ in range(100_000):
#         # Acquire the lock before touching shared state
#         with lock:
#             counter += 1
#         # Automatically releases the lock when exiting the 'with' block

# if __name__ == "__main__":
#     t1 = threading.Thread(target=safe_increment)
#     t2 = threading.Thread(target=safe_increment)
    
#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()
    
#     print(f"Final safe counter value: {counter}")
#     print("Expected value: 200,000")

def recursive_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return recursive_palindrome(string[1:-1])

# Our inputs
words = ["racecar", "python", "madam", "level", "developer"]

# Shared storage and a lock to prevent race conditions
results = {}
lock = threading.Lock()

def worker(task_id, word):
    is_pal = recursive_palindrome(word)
    
    with lock:
        results[task_id] = word, is_pal
        
 # Under the hood, a Python dict is a complex C-level hash table array. When you insert a new key-value pair, Python has to calculate hash values, check memory buckets, and potentially resize/reallocate the entire array if it gets too full.

# If Thread A and Thread B try to resize or modify the dictionary's internal buckets at the exact same microsecond, they step on each other's memory pointers.

# This can corrupt the dictionary's internal structure, leading to silent data loss, infinite loops, or crashes (like RuntimeError: dictionary changed size during iteration or segmentation faults).

threads = []

for i, word in enumerate(words):
    t = threading.Thread(target=worker, args=(f"task_{i}", word))
    threads.append(t) # reference
    t.start()


for t in threads:
    t.join()


print("All tasks completed. Results:")
for task_id, (word, is_pal) in results.items():
    print(f"{task_id} ('{word}'): Is palindrome? {is_pal}")

print()
print(threads)
