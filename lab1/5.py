import asyncio

async def fibonacci():
    fib_0 = 0
    print(fib_0)
    await asyncio.sleep(1)
    fib_1 = 1
    print(fib_1)
    await asyncio.sleep(1)
    while True:
        fib_n = fib_0 + fib_1
        print(fib_n)
        await asyncio.sleep(1)
        fib_0 = fib_1
        fib_1 = fib_n

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(fibonacci())

    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print("Przerwanie")

        tasks = asyncio.all_tasks(loop=loop)
        for task_ in tasks:
            task_.cancel()
        
        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        loop.close()