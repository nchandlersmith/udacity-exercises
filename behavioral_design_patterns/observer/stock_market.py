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
