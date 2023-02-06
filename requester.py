import aiohttp 
import datetime as dt
import company
import time
import json

text_file = open("api_key.json", "r")
rest_api_key = text_file.read()
rest_api_key = json.loads(rest_api_key)["api_key"]
text_file.close()

auth = aiohttp.BasicAuth(rest_api_key,"")

async def request(session, url, params=None):
    # Sometimes request fail (unstable server) we keep trying it until we get the response
    while True:
        async with session.get(url, auth=auth, params=params) as response:
            if response.status == 200:
                return await response.json()
        time.sleep(1) # we wait 1 second before the next try to avoid excessive retries and avoid to be blocked by the server
    
async def request_all_pages(session, url, items_per_page, total_results, params={}):
    items = []
    while True:
        pagination_params = {
            "start_index": len(items),
            items_per_page: 5000 # 5000 is the maximum items per page
        }
        params = {**params, **pagination_params} # joining two dictionaries
        response = await request(session, url, params)

        items += response["items"] # join the two lists
        if len(items) == int(response[total_results]):
            return items

# REST API to get incorporated companies from the last 60 days
async def get_latest_companies(session):
    incorporated_from = dt.date.today() - dt.timedelta(days=60)
    params = {
        "sic_codes": company.SIC_CODES,
        "company_status": ["open", "active"],
        "incorporated_from": str(incorporated_from)
    }
    return await request_all_pages(session, 'https://api.company-information.service.gov.uk/advanced-search/companies', "size", "hits", params)

async def get_company_registered_officer_names(session, company_number):
    return await request_all_pages(session, 'https://api.company-information.service.gov.uk/company/{}/officers'.format(company_number), "items_per_page", "total_results")
