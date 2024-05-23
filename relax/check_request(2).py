import asyncio
import aiohttp
from asyncio import Semaphore
import aiofiles
from time import perf_counter

THREAD = 20


async def downloader(url, filename, sm: Semaphore):
    try:
        async with sm:

            U = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                               " (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
            async with aiohttp.ClientSession() as s:
                async with s.get(url, headers=U) as res:
                    if res.status == 200:
                        async with aiofiles.open(filename, "wb") as f:
                            async for i in res.content.iter_chunked(2048):
                                await f.write(i)
                            print(f"Request to {url} was Successful")
                    else:
                        print("Error to find information of page")
    except Exception as e:
        print(f"SSSSSS -> {e}")

    finally:
        sm.release()


async def main():
    tasks = []
    semaphore = Semaphore(THREAD)
    async with aiofiles.open("urls.txt", 'r')as f:
        urls = await f.readlines()
        for url in urls:
            tasks.append(downloader(url, "test.txt", semaphore))
    await asyncio.gather(*tasks)

start = perf_counter()
asyncio.run(main())
end = perf_counter()

print(f"Total Time: {end - start:.3f}")
