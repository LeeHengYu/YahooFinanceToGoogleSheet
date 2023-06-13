# YahooFinanceToGoogleSheet
A python script that can crawl the current stock prices by reading the tickers on a Google Sheet, and print the prices back in Google Sheet.
Mostly generated by [ChatGPT](https://chat.openai.com/)

## Libraries
1. oauth2client.service_account
2. gspread
3. yahoo_fin (You may also use `yfinance`, but I don't know why that doesn't work on my machine.)

## Third-party service
Google Sheet API

## Configuration
Need to create a project in Google Cloud Console, get the credential json file and add the client email to common editor of the Google Sheet.

## Tickers
Cash is not a valid ticker so we set its value to 1.

## Currency
USD
