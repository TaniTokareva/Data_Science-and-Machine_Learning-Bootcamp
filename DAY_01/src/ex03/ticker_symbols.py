import sys

def ticker_symbols():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) == 2:
        ticker_symbol  = sys.argv[1].upper()
        if ticker_symbol in STOCKS:
            price = STOCKS[ticker_symbol]
            
            for item in COMPANIES:
                if COMPANIES[item] == ticker_symbol:
                    print(item, price)
        
        else: 
            print("Unknown ticker")


if __name__ == '__main__':
    ticker_symbols()
