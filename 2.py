import asyncio
import aiohttp

services = [
    "https://api.ipify.org",
    "http://ip-api.com/ip.php"
]


async def fetch_ip(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                ip = await response.text()
                return (ip, url)
    except Exception:
        return None


async def get_first_ip():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_ip(session, url)) for url in services]
        for completed in asyncio.as_completed(tasks):
            result = await completed
            if result:
                return result


ip, service = asyncio.run(get_first_ip())
print(f"Ваш IP: {ip} (Сервис: {service})")
