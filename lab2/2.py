import aiohttp
import asyncio


async def add_user(url: str, header: dict, body: dict) -> str:
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.post(url, data=body) as response:
            return await response.json()


async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    header = {"Token": "Bearer SOME_CHARS"}
    body = {
        "name": "Nowy uzytkownik",
        "avatar": "https://plus.unsplash.com/premium_photo-1683865776032-07bf70b0add1?q=80&w=1032&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    }
    user = await add_user(url=url, header=header, body=body)
    print(user)


if __name__ == "__main__":
    asyncio.run(main())
