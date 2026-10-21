import asyncio
import time
import httpx

async def check(client, url):
    try:
        start = time.perf_counter()
        response = await client.get(url, timeout=5, follow_redirects=True)
        taken = round(time.perf_counter() - start, 2)
        return {"url": url, "status": response.status_code, "time": taken}
    except Exception:
        return {"url": url, "status": "FAILED", "time": None}

async def main():
    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://wikipedia.org",
        "https://thissitedoesnotexist12345.com",
    ]
    total_start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[check(client, u) for u in urls])
    for r in results:
        print(r)
    print("Total:", round(time.perf_counter() - total_start, 2))

if __name__ == "__main__":
    asyncio.run(main())