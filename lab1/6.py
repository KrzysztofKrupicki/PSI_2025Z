import asyncio

async def fetch(delay: int):
    await asyncio.sleep(delay)
    return 10

async def main():
    result_fetch_1 = await fetch(3)
    print(result_fetch_1)
    result_fetch_2 = await fetch(1)
    print(result_fetch_2)
    result_fetch_3 = await fetch(6)
    print(result_fetch_3)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(main())

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