class Investor:
    def __init__(self, name):
        self._name = name
        self._notifications = []

    @property
    def notifications(self):
        return self._notifications

    def update(self, price):
        self._notifications.append(
            f"{self._name} notified: stock price is now {price}")
        print(f"{self._name} notified: stock price is now {price}")


class StockMarket():
    def __init__(self):
        self._subscribers = []

    @property
    def subscribers(self):
        return self._subscribers

    def subscribe(self, investor):
        self._subscribers.append(investor)

    def unsubscribe(self, investor):
        self.subscribers.remove(investor)

    def set_price(self, price):
        for subscriber in self.subscribers:
            subscriber.update(price)


if __name__ == "__main__":
    market = StockMarket()
    investor1 = Investor("1")
    investor2 = Investor("2")
    market.subscribe(investor1)
    market.subscribe(investor2)

    market.set_price(133.08)
    market.set_price(156.44)
    
    market.unsubscribe(investor2)

    market.set_price(144.22)