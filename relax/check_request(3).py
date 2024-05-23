import asyncio
import aiofiles
import aiohttp
from asyncio import Semaphore
from time import perf_counter
from bs4 import BeautifulSoup

Process = 13


async def downloader(url, filename, lock: Semaphore):
    H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                       " (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    try:
        async with lock:
            async with aiohttp.ClientSession() as s:
                async with s.get(url, headers=H) as res:
                    if res.status == 200 and res.status != 404:
                        html = await res.text()
                        doc = BeautifulSoup(html, "html.parser")
                        title = doc.select("title")[0].text
                        # filename = f"{url} : {title}"
                        # if title:
                        # print("Ok")
                        # async with aiofiles.open(filename, 'wb') as f:
                        #     async for chunk in res.content.iter_any():
                        #         await f.write(chunk)
                        # print(f"Request to {url} Was Successful")
                        async with aiofiles.open(filename, "a") as t:
                            await t.write(f"url: {url} -> title: {title}\n")
                            await t.truncate()
                        print(f"{url} -> {title}")
                    else:
                        raise FileNotFoundError

    except Exception as err:
        print(f"Error Message: {err}")

    finally:
        lock.release()


async def main():
    tasks = []
    urls = [
        'https://anisa.co.ir',
        'https://google.com',
        'https://yahoo.com',
        'https://digikala.com',
        'https://torob.com',
        'https://iranfoia.ir',
        'https://maktabkhooneh.org',
    ]
    sm = Semaphore(Process)
    for url in urls:
        tasks.append(downloader(url, "async_test.txt", sm))
    await asyncio.gather(*tasks)


start = perf_counter()
asyncio.run(main())
end = perf_counter()
print(f"Total Time: {end - start:.2f}")
