import asyncio

async def krojenieWarzyw(danie: str) -> None:
    print(f"{danie} - Krojenie warzyw rozpoczęte")
    await asyncio.sleep(2)
    print(f"{danie} - Krojenie warzyw zakończone")

async def gotowanieMakaronu(danie: str) -> None:
    print(f"{danie} - Gotowanie makaronu rozpoczęte")
    await asyncio.sleep(5)
    print(f"{danie} - Gotowanie makaronu zakończone")

async def smazenie(danie: str) -> None:
    print(f"{danie} - Smażenie rozpoczęte")
    await asyncio.sleep(3)
    print(f"{danie} - Smażenie zakończone")

async def kuchnia(danie: str) -> None:
    print(f"Kuchna danie: {danie}")
    await krojenieWarzyw(danie)
    await gotowanieMakaronu(danie)
    await smazenie(danie)
    print(f"Kuchna danie: {danie} - gotowe!")

async def main() -> None:
    await asyncio.gather(kuchnia('Danie 1'), kuchnia('Danie 2'), kuchnia('Danie 3'))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())