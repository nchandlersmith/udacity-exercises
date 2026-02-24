"""Test the stock market"""

from stock_market import Investor


class TestStockMarket:
    def test_investor_should_update_price(self):
        investor = Investor("Some investor")
        investor.update(247.16)
        
        result = investor.notifications
        
        assert len(result) == 1
        assert result[0] == "Some investor notified: stock price is now 247.16"
        
    