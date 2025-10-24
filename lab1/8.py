import asyncio

async def wczytaniePliku(nazwaPliku: str) -> None:
    print(f"Wczytywanie pliku {nazwaPliku}")
    await asyncio.sleep(2)

async def analizaPliku(nazwaPliku: str) -> None:
    print(f"Analizowanie pliku {nazwaPliku}")
    await asyncio.sleep(4)

async def zapisywaniePliku(nazwaPliku: str) -> None:
    print(f"Zapisywaie pliku {nazwaPliku}")
    await asyncio.sleep(1)

async def przetwarzaniePlikow(nazwaPliku: str) -> None:
    await wczytaniePliku(nazwaPliku)
    await analizaPliku(nazwaPliku)
    await zapisywaniePliku(nazwaPliku)
    print(f'Plik {nazwaPliku} przetworzony.')

async def main() -> None:
    pliki = [przetwarzaniePlikow("plik1"), przetwarzaniePlikow("plik2"), przetwarzaniePlikow("plik3"), przetwarzaniePlikow("plik4"), przetwarzaniePlikow("plik5")]
    await asyncio.gather(*pliki, return_exceptions=True)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())