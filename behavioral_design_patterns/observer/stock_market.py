class Investor:
    def __init__(self, name):
        self._name = name
        self._notifications = []
    
    @property
    def notifications(self):
        return self._notifications
    
    def update(self, price):
        self._notifications.append(f"{self._name} notified: stock price is now {price}")