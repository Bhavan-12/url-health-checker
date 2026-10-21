import asyncio
import httpx
from checker_async import check

def run_check(url):
    async def go():
        async with httpx.AsyncClient() as client:
            return await check(client, url)
    return asyncio.run(go())

def test_good_url():
    assert run_check("https://google.com")["status"] == 200

def test_bad_url():
    assert run_check("https://thissitedoesnotexist12345.com")["status"] == "FAILED"

def test_result_has_all_keys():
    result = run_check("https://google.com")
    assert set(result.keys()) == {"url", "status", "time"}