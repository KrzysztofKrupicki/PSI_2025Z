import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_weather(city: str, latitude: float, longitude: float) -> dict[str, str]:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    weather_data = await fetch(url)
    return {
        "city": city,
        "hours": weather_data["hourly"]["time"],
        "temperatures": weather_data["hourly"]["temperature_2m"],
        "wind_speeds": weather_data["hourly"]["wind_speed_10m"]
    }


async def get_weather_filtered(city: str, coords: list[float], mask: dict) -> tuple[str, str] | tuple[str, None]:
    weather = await get_weather(city, coords[0], coords[1])
    wind_speeds = weather["wind_speeds"]
    temperatures = weather["temperatures"]

    for wind, temp in zip(wind_speeds, temperatures):
        if "wind_speed_10m" in mask:
            condition = mask["wind_speed_10m"]
            symbol, value = condition.split(" ")

            if symbol == "<" and float(wind) < float(value):
                return city, temp
            if symbol == ">" and float(wind) > float(value):
                return city, temp

    return city, None


async def main() -> None:
    cities = {
        "Olsztyn": [53.7799, 20.4942],
        "Kraków": [50.0614, 19.9366],
        "Tokyo": [35.6895, 139.6917],
        "Alps": [47.2469, 9.3765],
        "San Andreas": [38.196, -120.6805]
    }

    mask = {"wind_speed_10m": "< 20"}

    tasks = [get_weather_filtered(city, coords,  mask) for city, coords in cities.items()]
    results = await asyncio.gather(*tasks)

    filtered = {city: temp for city, temp in results if temp is not None}
    print(filtered)


if __name__ == "__main__":
    asyncio.run(main())
