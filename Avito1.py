import time
import requests
import asyncio
import aiohttp
import re

def calculating(numbers):
    N = int(len(numbers) ** 0.5)
    list_i = list(range(0, N))
    list_j = list(range(0, N))
    sorted_numbers = list()
    last_j = 0
    last_i = 0
    for k in range(0, N):
        for i in list_i:
            sorted_numbers.append(int(numbers[last_j + i * N]))
        last_i = list_i[-1]
        list_j.pop(0)
        for j in list_j:
            sorted_numbers.append(int(numbers[j + last_i * N]))
        try:
            last_j = list_j[-1]
            list_i.reverse()
            list_j.reverse()
            list_i.pop(0)
        except:
            break
    return sorted_numbers

async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            data = await response.text()
            numbers = re.findall(r'[-+]?\d+', data)
            output = calculating(numbers)
            return output

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

loop = asyncio.get_event_loop()
def test_get_matrix():
    assert loop.run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL

test_get_matrix()
