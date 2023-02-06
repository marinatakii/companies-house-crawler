# companies-house-crawler

Automated solution that gets any relevant data about newly incorporated restaurants and shares them on a GSheet.

# File requirements

1. Create a file named `api_key.json` in the same folder of `crawler.py`:
```json
{
  "api_key": "apikeyhere"
}
```

2. Create a file named `gsheets.json` in the same folder of `crawler.py`:
```json
{
  "sheets_id": "googlesheetsidhere"
}
```
3. Make a copy of the GSheets' `credentials.json` in the same folder of `crawler.py`.
