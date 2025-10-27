import asyncio
import os
import aiohttp


async def download_file(url: str, path: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, "wb") as f:
                    while True:
                        chunk = await response.content.read(4096)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"Plik pobrany {path}")
            else:
                print(f"Nie można pobrać pliku, {response.status}")


async def main():
    url = input("Podaj url do pliku: ")
    # url = "https://enzomind.com/files/uwm/wyklady/ProjAppWeb/new_lab/lab_links.txt"
    dest_folder = input("Podaj ścieżkę do zapisu: ")
    file_name = input("Podaj nazwę dla pliku: ")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    file_path = os.path.join(dest_folder, file_name)

    await download_file(url, file_path)

if __name__ == "__main__":
    asyncio.run(main())
