import asyncio

async def maszynaA():
    czasPracy = 0
    while czasPracy < 15:
        print("A")
        await asyncio.sleep(2)
        czasPracy += 2

async def maszynaB():
    czasPracy = 0
    while czasPracy < 15:
        print("B")
        await asyncio.sleep(3)
        czasPracy += 3

async def maszynaC():
    czasPracy = 0
    while czasPracy < 15:
        print("C")
        await asyncio.sleep(5)
        czasPracy += 5

async def main():
    maszyny = [maszynaA(), maszynaB(), maszynaC()]
    await asyncio.gather(*maszyny)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

