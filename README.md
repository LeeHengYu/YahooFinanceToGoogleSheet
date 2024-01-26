# Yahoo Finance To Google Sheet
A python script that can fetch the current stock prices (inc. extended hours) by reading the tickers on a Google Sheet, and paste the prices back in Google Sheet.

Useful when sometimes GOOGLEFINANCE function is not working, or the real-time prices are needed.

## Libraries
1. `oauth2client.service_account`
2. `gspread`
3. `yahoo_fin` (You may also use `yfinance`, but I don't know why that doesn't work on my machine.)

## Third-party service
Google Sheet API

## Configuration
Need to create a project in Google Cloud Console, get the credential json file and add the client email to common editor of the Google Sheet.

## Tickers
Real-time quotes provided by **yahoo finance**

## Currency
USD
