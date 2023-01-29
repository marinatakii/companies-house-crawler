import requester

SIC_CODES = [56101, 56102, 56103]

class Company():
    def __init__(self, company_name, company_number, registered_office_address, date_of_creation, company_type, sic_codes, company_registered_officer_names, company_status):
        self.company_name = company_name
        self.company_number = company_number 
        self.registered_office_address = registered_office_address
        self.date_of_creation = date_of_creation
        self.company_type = company_type
        self.company_registered_officer_names = company_registered_officer_names
        self.sic_codes = sic_codes
        self.company_status = company_status

    # format texts
    def format_company_registered_officer_names(officers):
        names = []
        for officer in officers:
            names.append(officer["name"])
        return "; ".join(names) # We use ; as the separator to avoid confusion because the name is formatted as "SURNAME, Firstname"


    def format_sic_codes(sic_codes):
        return ", ".join(sic_codes)


    def format_registered_office_address(address):
        return "{}, {}, {}, {}".format(address.get("address_line_1", ""), address.get("locality", ""), address.get("postal_code",""), address.get("country", ""))


    async def from_item(session, item):
        company_name = item["company_name"]
        company_number = item["company_number"]
        registered_office_address = Company.format_registered_office_address(item["registered_office_address"])
        date_of_creation = item["date_of_creation"]
        company_type = item["company_type"]
        company_status = item["company_status"]
        company_registered_officer_names = Company.format_company_registered_officer_names(await requester.get_company_registered_officer_names(session, company_number)) 
        sic_codes = Company.format_sic_codes(item["sic_codes"])


        return Company(company_name, company_number, registered_office_address, date_of_creation, company_type, sic_codes, company_registered_officer_names, company_status)
