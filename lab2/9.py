import asyncio
import aiohttp


async def fetch(session: aiohttp.ClientSession, url: str) -> int | None:
    for attempt in range(3):
        async with session.get(url) as response:
            if 200 <= response.status <= 299:
                return response.status
            elif 500 <= response.status <= 599:
                print(f"Błąd ({response.status}), próba {attempt + 1}/3...")
                await asyncio.sleep(1)
            else:
                return None
    return None


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.7799&longitude=20.4942&hourly=temperature_2m"
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(100)]
        results = await asyncio.gather(*tasks)

    ok_responses = [status for status in results if status is not None]
    print(f"Ilość OK: {len(ok_responses)}")


if __name__ == "__main__":
    asyncio.run(main())
