"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession, ClientResponseError

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json_go(url: str) -> dict:
    try:
        async with ClientSession() as session:
            async with session.get(url, timeout=60) as response:
                resp = await response.json()
    except ClientResponseError as e:
        print(e.message)
        raise e
    else:
        return resp
