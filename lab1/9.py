import asyncio


async def maszynaA() -> None:
    while True:
        print("Maszyna A zaczyna cykl")
        await asyncio.sleep(2)
        print("Maszyna A kończy cykl")


async def maszynaB() -> None:
    while True:
        print("Maszyna B zaczyna cykl")
        await asyncio.sleep(3)
        print("Maszyna B kończy cykl")


async def maszynaC() -> None:
    while True:
        print("Maszyna C zaczyna cykl")
        await asyncio.sleep(5)
        print("Maszyna C kończy cykl")


async def main() -> None:
    zad_maszynaA = asyncio.create_task(maszynaA())
    zad_maszynaB = asyncio.create_task(maszynaB())
    zad_maszynaC = asyncio.create_task(maszynaC())
    await asyncio.sleep(15)
    zad_maszynaA.cancel()
    zad_maszynaB.cancel()
    zad_maszynaC.cancel()
    await asyncio.gather(zad_maszynaA, zad_maszynaB, zad_maszynaC, return_exceptions=True)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
