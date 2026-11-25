import asyncio

# import random

# lexicon = {
#     1: "first",
#     2: "Second",
#     3: "third",
#     4: "fourth",
#     5: "fifth"
# }

# # Shared counter and lock to safely track completion order
# finish_order = 1
# lock = asyncio.Lock()

# async def sleep_1():
#     global finish_order
#     random_num = random.randint(1, 5)
#     await asyncio.sleep(random_num)
    
#     async with lock:
#         rank = finish_order
#         finish_order += 1
        
#     print(f"sleep_1 finished {lexicon[rank]}")
#     return f"sleep_1: {lexicon[rank]}"

# async def sleep_2():
#     global finish_order
#     random_num = random.randint(1, 5)
#     await asyncio.sleep(random_num)
    
#     async with lock:
#         rank = finish_order
#         finish_order += 1
        
#     print(f"sleep_2 finished {lexicon[rank]}")
#     return f"sleep_2: {lexicon[rank]}"

# async def sleep_3():
#     global finish_order
#     random_num = random.randint(1, 5)
#     await asyncio.sleep(random_num)
    
#     async with lock:
#         rank = finish_order
#         finish_order += 1
        
#     print(f"sleep_3 finished {lexicon[rank]}")
#     return f"sleep_3: {lexicon[rank]}"

# async def sleep_4():
#     global finish_order
#     random_num = random.randint(1, 5)
#     await asyncio.sleep(random_num)
    
#     async with lock:
#         rank = finish_order
#         finish_order += 1
        
#     print(f"sleep_4 finished {lexicon[rank]}")
#     return f"sleep_4: {lexicon[rank]}"
    
# async def sleep_5():
#     global finish_order
#     random_num = random.randint(1, 5)
#     await asyncio.sleep(random_num)
    
#     async with lock:
#         rank = finish_order
#         finish_order += 1
        
#     print(f"sleep_5 finished {lexicon[rank]}")
#     return f"sleep_5: {lexicon[rank]}"

# async def main_():
#     res = await asyncio.gather(
#         sleep_1(),
#         sleep_2(),
#         sleep_3(),
#         sleep_4(),
#         sleep_5(),
#     )
    
#     print("\nFinal Results Summary:")
#     print(res)

# # This starts the event loop
# asyncio.run(main_())


async def fetch_data(server_name: str, delay: int) -> str:
    print(f"Starting {server_name}")
    await asyncio.sleep(delay)
    print(f"Received data from {server_name}")

    return server_name


async def main():
    # task_1 = await asyncio.create_task(fetch_data("server_A", 2))
    # task_2 = await asyncio.create_task(fetch_data("server_B", 1))
    
    task_1, task_2 = await asyncio.gather(fetch_data("server_A", 2), fetch_data("server_B", 1))
    print("All data fetched", task_1, task_2)

asyncio.run(main=main())    


# As you build more, you will occasionally run into a few extra tools for edge cases. Here is a quick cheat sheet of what else asyncio has in store for when you need it later:

# asyncio.wait_for(task, timeout=5): Automatically cancels a task if it takes too long (prevents your app from hanging forever on a slow network request).

# asyncio.Semaphore(n): Limits how many tasks can run at the exact same time (great for preventing you from overwhelming a database or getting banned by an API for hitting it with 1,000 requests at once).

# asyncio.Queue(): Lets different coroutines safely pass data to each other in a pipeline (one coroutine downloads data, puts it in the queue, and another coroutine pulls it out to process it).
