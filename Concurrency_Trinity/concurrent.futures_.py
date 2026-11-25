import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def recursive_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return recursive_palindrome(string[1:-1])

words = ["racecar", "python", "madam", "level", "developer"]

with ThreadPoolExecutor(max_workers=3) as executor:
    res = executor.map(recursive_palindrome, words)
    
    # for value in res, words:
    #     print(value)
# print(list(res))

def slow_task(name):
    delay = random.randint(1, 9)
    time.sleep(delay)
    return f"Task {name} finished in {delay}s"

tasks = ["A", "B", "C"]

with ThreadPoolExecutor(max_workers=3) as executor:
     # Submit tasks individually and get back "Future" objects
    future_to_task = {executor.submit(slow_task, t): t for t in tasks}
    # print(future_to_task)
    
    # As each thread finishes, catch its result immediately
    for future in future_to_task:
        try:
            result = future.result()
            print(result)
        except Exception as exc:  # noqa: BLE001, RUF100
            print(f"Task generated an exception: {exc}")


with ThreadPoolExecutor() as executor:
    future_to_task = [executor.submit(slow_task, t) for t in tasks]
    
    # future_1 = executor.submit(slow_task, "A")
    # future_2 = executor.submit(slow_task, "B")
    # future_3 = executor.submit(slow_task, "C")
    # print(future_1.result())
    # print(future_2.result())
    # print(future_3.result())
    
    for future in as_completed(future_to_task):
        print(future.result()) # freezes the main thread till this is done


# backup
