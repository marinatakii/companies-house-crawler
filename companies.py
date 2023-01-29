import requester
import asyncio
from company import Company

class Companies:
    def __init__(self):
        self.list = []

    async def get_latest(session):
        companies = Companies()
        items = await requester.get_latest_companies(session)

        # Loop for making 600 requests each 5 minutes (API limit rate)
        total = len(items)
        while True:
            slice = items[0:total][-600:] # gets a slice of the last 600 companies in the 0..total range
            total -= len(slice) # decrease by the total number of companies we are processing so we don't pick them again
            futures = []
            for item in slice:
                company = Company.from_item(session, item)
                futures.append(company)
            companies.list += await asyncio.gather(*futures)
            if total == 0: # if total == 0, we have processed all the companies.
                return companies
            else: # we wait 5 minutes before processing the next 600 (or less) companies
                await asyncio.sleep(60 * 5)
