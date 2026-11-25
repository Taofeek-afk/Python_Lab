import multiprocessing as mp
from multiprocessing import shared_memory


def update_shared(counter: mp.Value, nums: mp.Array, lock: mp.Lock, idx: int) -> None: # type: ignore
    with lock:
        counter.value += 1
        nums[idx] = nums[idx] * 2


if __name__ == "__main__":
    ctx = mp.get_context("fork")
    counter = ctx.Value("i", 0)       # 'i' = signed C integer
    nums = ctx.Array("i", [2, 4, 6])  # shared array of 3 C integers
    lock = ctx.Lock()

    procs = [
        ctx.Process(target=update_shared, args=(counter, nums, lock, i))
        for i in range(len(nums))
    ]
    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print("counter:", counter.value)  # 3
    print("nums:", list(nums))        # type: ignore # [4, 8, 12]
    


def worker(
    counter: mp.Value, # type: ignore
    arr: mp.Array, # type: ignore
    shm_name: str,
    lock: mp.Lock, # type: ignore
    idx: int,
) -> None:
    # Attach to the shared byte buffer created in the parent
    shm = shared_memory.SharedMemory(name=shm_name, create=False)
    try:
        with lock:
            # 1. Shared C int via Value
            counter.value += 1

            # 2. Shared C int array via Array
            arr[idx] += 10

            # 3. Shared raw bytes via SharedMemory (same underlying buffer across processes)
            shm.buf[idx] = shm.buf[idx] + 1 # type: ignore
    finally:
        shm.close()


if __name__ == "__main__":
    ctx = mp.get_context("fork")
    lock = ctx.Lock()

    counter = ctx.Value("i", 0)
    arr = ctx.Array("i", [1, 2, 3, 4])

    # 4 bytes in shared memory, initialized to [10, 20, 30, 40]
    shm = shared_memory.SharedMemory(create=True, size=4)
    try:
        shm.buf[:] = bytes([10, 20, 30, 40]) # type: ignore

        procs = [
            ctx.Process(target=worker, args=(counter, arr, shm.name, lock, i))
            for i in range(4)
        ]
        for p in procs:
            p.start()
        for p in procs:
            p.join()

        print("counter:", counter.value)       # 4
        print("arr:", list(arr))               # type: ignore # [11, 12, 13, 14]
        print("shm.buf:", list(shm.buf[:4]))   # type: ignore # [11, 21, 31, 41]
    finally:
        shm.close()
        shm.unlink()  # Always unlink shared memory when finished