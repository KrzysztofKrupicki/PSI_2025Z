import asyncio

async def wczytaniePliku(nazwaPliku):
    print(f"Wczytywanie pliku {nazwaPliku}")
    await asyncio.sleep(2)

async def analizaPliku(nazwaPliku):
    print(f"Analizowanie pliku {nazwaPliku}")
    await asyncio.sleep(4)

async def zapisywaniePliku(nazwaPliku):
    print(f"Zapisywaie pliku {nazwaPliku}")
    await asyncio.sleep(1)

async def przetwarzaniePlikow(nazwaPliku):
    await wczytaniePliku(nazwaPliku)
    await analizaPliku(nazwaPliku)
    await zapisywaniePliku(nazwaPliku)

async def main():
    pliki = [przetwarzaniePlikow("plik1"), przetwarzaniePlikow("plik2"), przetwarzaniePlikow("plik3"), przetwarzaniePlikow("plik4"), przetwarzaniePlikow("plik5")]
    await asyncio.gather(*pliki, return_exceptions=True)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())