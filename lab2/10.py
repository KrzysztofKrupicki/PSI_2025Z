from datetime import datetime, timezone
from typing import Any, Coroutine

import aiohttp
import asyncio
import json

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def process_weather_data(data: dict) -> dict[str, int | str | Any] | dict[Any, Any]:
    hours = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    current_hour = datetime.now().hour
    processed_data = {}
    for time, temp in zip(hours, temperatures):
        forecast_time = datetime.fromisoformat(time)
        if forecast_time.hour == current_hour:
            processed_data = {
                "forecast_hour": forecast_time.hour,
                "forecast_temp": temp,
                "received_at": datetime.now().isoformat(),
            }
    return processed_data

async def save_file(filename: str, data: dict[str, int | str | Any]) -> None:
    with open("weather_data.txt", "a") as file:
        file.write(json.dumps(data) + "\n")

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&forecast_days=1"
    weather_data = await fetch(url)
    processed_data = await process_weather_data(weather_data)
    if processed_data:
        await save_file("weather_data.json", processed_data)
        print('Data saved to weather_data.txt')
    else:
        print('No data for current hour found.')

if __name__ == "__main__":
    asyncio.run(main())