from datetime import datetime

import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&forecast_days=1"
    weather_data = await fetch(url)

    hours = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]

    current_hour = datetime.now().hour

    for i, hour in enumerate(hours):
        forecast_time = datetime.fromisoformat(hour)
        if forecast_time.hour == current_hour:
            print(f"Temperatura dla Zakopanego na najblizsza godzine ({forecast_time.hour}:00): {temperatures[i]}°C")
            return

if __name__ == "__main__":
    asyncio.run(main())