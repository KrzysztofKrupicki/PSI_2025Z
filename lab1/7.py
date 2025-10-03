import asyncio

async def krojenieWarzyw():
    print("Krojenie warzyw")
    await asyncio.sleep(2)

async def gotowanieMakaronu():
    print("Gotowanie makaronu")
    await asyncio.sleep(5)

async def smazenie():
    print("Smażenie")
    await asyncio.sleep(3)

async def kuchnia():
    await krojenieWarzyw()
    await gotowanieMakaronu()
    await smazenie()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(kuchnia())

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