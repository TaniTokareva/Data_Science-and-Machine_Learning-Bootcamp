import httpx
from bs4 import BeautifulSoup
import sys
import time
import pstats
import profile

def get_financial_data(ticker, field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials/'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        page = httpx.get(url, headers=headers)
        page.raise_for_status()
    except httpx.RequestError as e:
        raise Exception(f"Ошибка при получении страницы: {e}")

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
def main():
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

if __name__ == "__main__":
    try:
        profile_stats = profile.Profile()
        profile_stats.run("main()")

        stats = pstats.Stats(profile_stats)
        stats.sort_stats("cumtime").print_stats(5)
    except Exception as err:
        print(type(err).__name__, err, sep=': ')


#python -m cProfile -s time financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
#python -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
#python financial_enhanced.py 'MSFT' 'Total Revenue' > pstats-cumulative.txt