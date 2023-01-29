import gspread
import datetime

text_file = open("gsheets_id.txt", "r")
SHEETS_ID = text_file.read()
text_file.close()

class GSheets():
    def __init__(self):
        self.gc = gspread.service_account(filename='credentials.json')
        self.sh = self.gc.open_by_key(SHEETS_ID)
        self.ws = self.sh.worksheet('Page1')

    def update(self, companies):
        values = []
        for company in companies.list:
            values.append(list(company.__dict__.values()))
        self.ws.update('A1', [["Updated time", str(datetime.datetime.now())]]) # time that the sheets was updated
        self.ws.update('A2', [list(companies.list[0].__dict__.keys())]) # column names
        self.ws.update('A3', values)

