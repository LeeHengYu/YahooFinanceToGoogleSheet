# Yahoo Finance To Google Sheet
A python script that can fetch the current stock prices (excluding extended hours) by reading the tickers on a Google Sheet, and paste the prices back in Google Sheet.

Useful when sometimes GOOGLEFINANCE function is not working, or the real-time prices are needed.

## Libraries (pre-requisites)
1. `oauth2client.service_account`
2. `gspread`
3. `yfinance`

## Third-party service
Google Sheet API

## Configuration
Set up a Google Cloud Platform (GCP) project:

1. Go to the GCP Console (https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the Google Sheets API:
- In the left sidebar, click on "APIs & Services" > "Library".
- Search for "Google Sheets API" and enable it.
2. Create credentials:
- In the left sidebar, click on "APIs & Services" > "Credentials".
- Click on "Create credentials" and select "Service account".
- Fill in the required information and click on "Create".
- Download the JSON file containing your service account credentials.
3. Store your credential json file in the working folder with `main_publish.py`.
4. Add the google sheet API helper writer (an email address) editors.

## Quick Start
1. Change the constant variables in line 5 - 9
2. Run the file

## Tickers
Real-time quotes provided by **yahoo finance**

## Currency
USD
