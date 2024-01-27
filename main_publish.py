import gspread
import yfinance as yf
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIAL_PATH = "credentials.json" # relative path
SHEET_TITLE = 'Your Google Sheet Title'
SHEET_NAME = 'Your Sheet Name'
TICKER_RANGE = 'A1:A10' # 1d range
PRICE_RANGE = 'C1:C10' # 1d range

def verify_credential(credential_path):
    # Set up Google Sheets credentials
    SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_path, SCOPE)
    conn = gspread.authorize(credentials)
    return conn

def connect_to_sheet(client, title: str, sheet: int | str):
# Open the Google Sheet
    if type(sheet) == int:
        s = client.open(title).get_worksheet(sheet)
    else:
        s = client.open(title).worksheet(sheet)
    return s

def get_price(tickers: list[str]):
    tickers_copy = tickers.copy()
    tickers_copy.pop(tickers_copy.index("Cash"))
    data = yf.download(tickers_copy, period='1m', interval='60m', group_by="Ticker")
    quote = { ticker: data[(ticker, 'Close')][-1] for ticker in tickers_copy }
    quote['Cash'] = 1
    quote['cash'] = 1
    return quote

def update_prices(sheet, ticker_range: str, price_range: str, rounding: int = 3):
    tickers = sheet.get(ticker_range)
    tickers = [ticker[0] for ticker in tickers]
    download = get_price(tickers)
    prices = [download.get(tick, 0) for tick in tickers]
    update_range = sheet.range(price_range)
    assert len(prices) == len(update_range)
    
    for price, cell in zip(prices, update_range):
        cell.value = round(price, rounding)
        
    sheet.update_cells(update_range)
    
    
if __name__ == '__main__':
    conn = verify_credential(CREDENTIAL_PATH)
    sheet = connect_to_sheet(conn, SHEET_TITLE, SHEET_NAME)
    update_prices(sheet, TICKER_RANGE, PRICE_RANGE)    