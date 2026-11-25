import multiprocessing as mp
import os

pid = os.getpid()
print(pid)

def worker(n: int) -> int: # type: ignore
    print(f"pid={os.getpid()} computing {n}*{n}")
    return n * n


if __name__ == "__main__":
    ctx = mp.get_context("fork")
    
    with ctx.Pool(processes=4) as pool:
        results = pool.map(worker, [1, 2, 3, 4, 5])

    print("Results:", results)

print()

# Inherited read-only by forked children without pickling
LOOKUP_TABLE = {1: 10, 2: 20, 3: 30, 4: 40}


def compute_item(key: int, out_queue: mp.Queue, lock: mp.Lock) -> None: # type: ignore
    value = LOOKUP_TABLE.get(key, 0) * 2
    with lock:
        # Synchronizes access to stdout or another shared resource
        out_queue.put((key, value))
# A704-6E97
if __name__ == "__main__":
    ctx = mp.get_context("fork")
    queue = ctx.Queue()
    lock = ctx.Lock()
# EDEE-EE24
    processes = [
        ctx.Process(target=compute_item, args=(k, queue, lock))
        for k in LOOKUP_TABLE
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    outputs = [queue.get() for _ in processes]
    print("Collected:", sorted(outputs))
    print(outputs)


def compute_item(key, connection): # type: ignore
    value = LOOKUP_TABLE.get(key, 0) * 2
    connection.send((key, value))
    connection.close()

if __name__ == "__main__":
    ctx = mp.get_context("fork")

    parent_conn, child_conn = ctx.Pipe()
    # print(ctx.Pipe)
    p = ctx.Process(
        target=compute_item,
        args=(1, child_conn)
    )

    p.start()
    child_conn.close()
# - parent_conn: the parent's receiving endpoint.
# - child_conn: the child's sending endpoint.
# - child_conn.close() in the parent: closes only the parent's reference to the child's endpoint.
    result = parent_conn.recv()
# listen for incoming data through the parent's endpoint.
# If no data is available, wait (block).
# When data arrives, receive it.
# Deserialize it.
# Return the resulting Python object.

    p.join()

    print(result)  # (1, 20)


from concurrent.futures import ProcessPoolExecutor

LOOKUP_TABLE = {1: 10, 2: 20, 3: 30, 4: 40}

def compute_item(key):
    return key, LOOKUP_TABLE.get(key, 0) * 2

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_item, LOOKUP_TABLE)

        print(list(results))

counter = 100

def worker(): # type: ignore
    global counter

    counter += 50
    print("Child:", counter)

if __name__ == "__main__":
    ctx = mp.get_context("fork")

    p = ctx.Process(target=worker)
    p.start()
    p.join()

    print("Parent:", counter)


def worker(key, connection):
    result = key * 10
    connection.send(result)
    connection.close()

if __name__ == "__main__":
    ctx = mp.get_context("spawn")

    connections = []
    processes = []

    for key in range(1, 4):
        parent_conn, child_conn = ctx.Pipe()

        p = ctx.Process(
            target=worker,
            args=(key, child_conn)
        )

        p.start()
        child_conn.close()

        connections.append(parent_conn)
        processes.append(p)

    results = [conn.recv() for conn in connections]

    for p in processes:
        p.join()

    print(results)