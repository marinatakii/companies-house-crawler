import aiohttp
import asyncio
from gsheets import GSheets
from companies import Companies 
import platform
import time

# Windows specific fix
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        companies = await Companies.get_latest(session)
        gsheets = GSheets()
        gsheets.update(companies)
        end_time = time.time()
        duration = end_time - start_time
        print("Execution duration:", duration)

asyncio.run(main())
