import time
import requests
import asyncio
import aiohttp
import re

async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            data = await response.text()
            c = re.findall(r'[-+]?\d+', data)
            indexes = [1, 5, 9, 13,
                       14, 15, 16, 12,
                       8, 4, 3, 2,
                       6, 10, 11, 7]

            def get_numb(i):
                return int(c[i - 1])
            output = list(map(get_numb, indexes))
            print(output)

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
# TRAVERSAL = [
#     10, 50, 90, 130,
#     140, 150, 160, 120,
#     80, 40, 30, 20,
#     60, 100, 110, 70,
# ]

loop = asyncio.get_event_loop()
loop.run_until_complete(get_matrix(SOURCE_URL))