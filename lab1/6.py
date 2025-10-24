import asyncio
import random

async def fetch(delay: int):
    await asyncio.sleep(delay)
    random_value = random.randint(1, 100)
    print(f'Delay: {delay}, random value: {random_value}')
    return random_value

async def main():
    await asyncio.gather(fetch(4), fetch(1), fetch(3))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())