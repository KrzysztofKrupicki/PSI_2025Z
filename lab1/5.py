import asyncio

async def fibonacci(N: int) -> None:
    a = 0
    b = 1
    time = 0
    while time < N:
        print(a)
        await asyncio.sleep(1)
        a, b = b, a + b
        time += 1

async def main() -> None:
    N = int(input("Ilość sekund: "))
    await asyncio.gather(fibonacci(N))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())