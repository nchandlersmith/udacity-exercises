"""Test the stock market"""

from stock_market import Investor, StockMarket


class TestStockMarket:
    def test_investor_should_update_price(self):
        investor = Investor("Some investor")
        investor.update(247.16)

        result = investor.notifications

        assert len(result) == 1
        assert result[0] == "Some investor notified: stock price is now 247.16"

    def test_stock_market_subscribe(self):
        market = StockMarket()
        investor = Investor("")
        
        market.subscribe(investor)
        
        assert len(market.subscribers) == 1
        assert market.subscribers[0] == investor
        
        
    def test_stock_market_unsubscribe(self):
        market = StockMarket()
        investor1 = Investor("1")
        investor2 = Investor("2")
        market._subscribers.append(investor1)
        market._subscribers.append(investor2)
        
        market.unsubscribe(investor1)
        
        assert len(market.subscribers) == 1
        assert market.subscribers[0] == investor2
