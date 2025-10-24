import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    urls = [
        "https://api.dictionaryapi.dev/api/v2/entries/en/hello",
        "https://pokeapi.co/api/v2/pokemon/ditto",
        "https://rickandmortyapi.com/api/character",
        "https://dog.ceo/api/breed/affenpinscher/images/random",
        "https://v2.jokeapi.dev/joke/Any"
    ]

    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
