from datetime import datetime

import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_weather(city: str, latitude: float, longitude: float) -> float:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=1"
    weather_data = await fetch(url)
    hours = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    current_hour = datetime.now().hour

    for i, hour in enumerate(hours):
        forecast_time = datetime.fromisoformat(hour)
        if forecast_time.hour == current_hour:
            return float(temperatures[i])


async def main() -> None:
    cities = {
        "Porlamar": [10.95, -63.87],
        "Moroni": [1.69, 43.24],
        "Helsinki": [60.1695, 24.9354]
    }

    tasks = []
    for city, coords in cities.items():
        task = get_weather(city, coords[0], coords[1])
        tasks.append(task)

    temperatures = await asyncio.gather(*tasks)

    result = dict(zip(cities.keys(), temperatures))
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
