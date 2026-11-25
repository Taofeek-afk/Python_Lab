import asyncio
import threading
import time


def blocking_disk_or_legacy_work(item: int) -> str:
    # Runs inside a worker thread, NOT the asyncio event loop thread
    tid = threading.get_ident()
    time.sleep(0.5)  # Simulates blocking work
    return f"item={item} done on worker_thread={tid}"


async def heartbeat(loop_tid: int) -> None:
    # Runs on the main asyncio event loop thread
    for i in range(3):
        await asyncio.sleep(0.2)
        print(f"Event loop alive (tid={loop_tid}) tick {i + 1}")


async def main() -> None:
    loop_tid = threading.get_ident()
    print(f"Main / event loop thread id: {loop_tid}")

    # Run heartbeat on the event loop while blocking work runs in a worker thread
    hb_task = asyncio.create_task(heartbeat(loop_tid))
    result = await asyncio.to_thread(blocking_disk_or_legacy_work, 42)
    await hb_task

    print(result)


if __name__ == "__main__":
    asyncio.run(main())