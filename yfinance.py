import gspread
from oauth2client.service_account import ServiceAccountCredentials
from yahoo_fin import stock_info as si

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("`Your path to the credential json file`", scopes=scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('`name of the file`').worksheet("`name of the sheet`")

# Get the stock tickers from A2:A17
tickers = sheet.get('A2:A17')
ticker_values = [ticker[0] for ticker in tickers]

# Fetch the current stock prices
prices = []
for ticker in ticker_values:
    if ticker=="Cash":
        prices.append(1)
    else:
        current_price = si.get_live_price(ticker)  # Fetch the current market price
        prices.append(round(current_price, 3))

# Update cells C2:C17 with the stock prices
cell_range = sheet.range('C2:C17')
for i, cell in enumerate(cell_range):
    cell.value = prices[i]
    print(ticker_values[i],prices[i])

sheet.update_cells(cell_range)

# default currency: USD
