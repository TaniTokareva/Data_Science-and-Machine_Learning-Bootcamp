import sys

def stock_price():
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
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments")
    else:
        name = sys.argv[1].capitalize()
        if name in COMPANIES:
            key_1 = COMPANIES[name]
            key_2 = STOCKS[key_1]
            print(key_2)
        else: 
            print("Unknown company")


if __name__ == '__main__':
    stock_price()
