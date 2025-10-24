import asyncio

async def foo1():
    await asyncio.sleep(3)
    print("Korutyna foo1")

async def foo2():
    await asyncio.sleep(1)
    print("Korutyna foo2")

async def main():
    await asyncio.gather(foo1(), foo2())

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())