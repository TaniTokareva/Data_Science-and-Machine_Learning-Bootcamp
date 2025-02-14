import sys

def all_stocks():
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
        arg_string = sys.argv[1].strip()
        if ',,' in arg_string:
            return 

        words = [word.strip() for word in arg_string.split(',')]
        if '' in words:
            return
        # print(words)
        for word in words:
            if word.capitalize() in COMPANIES:
                company_name = word.capitalize()
                ticker = COMPANIES[company_name]
                price = STOCKS[ticker]
                print(company_name, "stock price is", price)
            elif word.upper() in STOCKS:
                ticker = word.upper()
                for company_name, item in COMPANIES.items():
                    if item == ticker:
                        print(ticker, "s a ticker symbol for", company_name)
            else: print(word, "is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()