#pytest financial_test.py
import pytest
from financial import get_financial_data

def test_get_financial_data_valid_ticker():
    ticker = "AAPL"
    field = "Total Revenue"
    result = get_financial_data(ticker, field)
    assert result is not None
    assert len(result) > 0
    assert result[0] == field


def test_get_financial_data_return_type():
    ticker = "AAPL"
    field = "Total Revenue"
    result = get_financial_data(ticker, field)
    assert isinstance(result, tuple)


def test_get_financial_data_invalid_ticker():
    ticker = "INVALID_TICKER"
    field = "Total Revenue"
    
    with pytest.raises(Exception): 
        get_financial_data(ticker, field)


def test_get_financial_data_invalid_field():
    ticker = "AAPL"
    field = "Invalid Field"  
    
    with pytest.raises(Exception): 
        get_financial_data(ticker, field)
