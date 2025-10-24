import asyncio

async def hello_world() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(1)
    print("world")

async def main() -> None:
    await hello_world()

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())