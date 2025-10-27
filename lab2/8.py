import datetime

import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_avg_tomorrow_temperature(city: str, latitude: float, longitude: float) -> float | None:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=2"
    weather_data = await fetch(url)
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    hours = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    tomorrow_temperatures = [temperature for hour, temperature in zip(hours, temperatures) if
                             hour.startswith(tomorrow.isoformat())]
    if not tomorrow_temperatures:
        return None
    avg_temperature = round(sum(tomorrow_temperatures) / len(tomorrow_temperatures), 1)
    return avg_temperature


async def main() -> None:
    cities = {
        "Porlamar": [10.9577, -63.8697],
        "Moroni": [1.69, 43.24],
        "Helsinki": [60.1695, 24.9354],
        "Praga": [50.0755, 14.4378],
        "Budapeszt": [47.4979, 19.0402],
        "Warszawa": [52.2297, 21.0122],
        "Berlin": [52.5200, 13.4050]
    }

    tasks = [get_avg_tomorrow_temperature(city, coords[0], coords[1]) for city, coords in cities.items()]
    temperatures = await asyncio.gather(*tasks)
    result = {city: temp for city, temp in zip(cities.keys(), temperatures) if temp is not None}
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
