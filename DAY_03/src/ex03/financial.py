#python financial.py "NOK" "Gross Profit"

import requests
from bs4 import BeautifulSoup
import sys
import time

def get_financial_data(ticker, field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code != 200:
        raise Exception(f"Error: Unable to fetch the page for {ticker}. Status code {page.status_code}")

    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticker')

    table = soup.find('div', class_="tableContainer")
    if not table:
        raise Exception(f"Error: No financial table found for {ticker}")

    new = table.find('div', class_='tableBody')
    if not new:
        raise Exception(f"Error: No table body found for {ticker}")

    rows = new.find_all('div', class_='row')
    if not rows:
        raise Exception(f"Error: No rows found in the financial table for {ticker}")

    data = None
    for row in rows:
        what_in_cell = row.find_all('div', class_='column')
        individuals_row_data = [data.text.strip() for data in what_in_cell]

        if individuals_row_data[0] == field:
            data = individuals_row_data
            break

    if not data:
        raise Exception(f"Error: Field '{field}' not found for {ticker}")
    
    return tuple(data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python financial.py <ticker> <field>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]
    time.sleep(5)
    try:
        print(get_financial_data(ticker, field))
    except Exception as e:
        print(str(e))